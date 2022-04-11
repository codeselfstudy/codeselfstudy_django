import os
import json
import logging
import pathlib
import subprocess
from typing import Dict
from urllib.parse import parse_qs

from helpers.utils import safe_list_get

log = logging.getLogger(__name__)


def is_valid_slack_app(qs):
    """
    Checks to see if the request is being made by a valid Slack app.
    """
    data = parse_qs(qs)
    return safe_list_get(data["api_app_id"], 0) == os.environ.get("SLACK_APP_ID")


def extract_slack_payload(payload):
    """
    Extract the form encoded data from slack into a dict.

    Example payload:

    token=gIkuxxxxxxxxxxxxxxxxgjtO <- don't use this
    &team_id=T0001
    &team_domain=example
    &enterprise_id=E0001
    &enterprise_name=Globular%20Construct%20Inc
    &channel_id=C2xxxxxxx05
    &channel_name=test
    &user_id=U21xxxxxx97
    &user_name=Steve
    &command=/weather
    &text=94070 <- this will be the payload
    &response_url=https://hooks.slack.com/commands/1234/5678
    &trigger_id=13xxxxxxx09.73xxxx920.8xxxxxxxxxxx8f008e0
    &api_app_id=A123456

    We'll probably want these items:

    user_name=josh
    text=codewars+6kyu+javascript+elixir+python+200votes+10stars <- parse this
    api_app_id=os.environ.get("SLACK_APP_ID")
    """
    data = parse_qs(payload)
    result = {
        "user_id": safe_list_get(data.get("user_id", None), 0, None),
        "user_name": safe_list_get(data.get("user_name", None), 0, None),
        "text": safe_list_get(data.get("text", None), 0, None),
        "response_url": safe_list_get(data.get("response_url", None), 0, None),
        "channel_name": safe_list_get(data.get("channel_name", None), 0, None),
        "channel_id": safe_list_get(data.get("channel_id", None), 0, None),
        "command": safe_list_get(data.get("command", None), 0, None),
    }
    return result


def parse_command(command: str) -> Dict:
    """
    Parses the command string into a Python dict.

    This uses the Raku parser.
    """
    current_dir = pathlib.Path().absolute()

    # The path needs modification here because it was overridden in order to
    # put the Django apps in their own directory.
    result = subprocess.run(
        [
            "raku",
            f"{current_dir}/apps/slack/command_parser/CommandParser.rakumod",
            command,
        ],
        capture_output=True,
    )
    log.info(f"result from raku is: {result}")
    j = result.stdout.decode("utf-8")
    d = json.loads(j)
    return d
