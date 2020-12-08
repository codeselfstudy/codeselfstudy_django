import os
from urllib.parse import parse_qs

from codeselfstudy.helpers.utils import safe_list_get


def is_valid_slack_app(qs):
    """
    Checks to see if the request is being made by a valid Slack app.
    """
    data = parse_qs(qs)
    return safe_list_get(data["api_app_id"], 0) == os.environ.get("SLACK_APP_ID")
