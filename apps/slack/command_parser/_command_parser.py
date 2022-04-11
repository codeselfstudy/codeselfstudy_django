"""
This module parses the Slack `/puzzle` command.

TODO: it was copied from the old Flask app and needs to be fixed for Django.
"""
import re
from os import environ
from helpers.utils import safe_list_get
from urllib.parse import parse_qs

from .languages import codewars_valid_languages

# Example payload:
#
# token=gIkuxxxxxxxxxxxxxxxxgjtO <- don't use this
# &team_id=T0001
# &team_domain=example
# &enterprise_id=E0001
# &enterprise_name=Globular%20Construct%20Inc
# &channel_id=C2xxxxxxx05
# &channel_name=test
# &user_id=U21xxxxxx97
# &user_name=Steve
# &command=/weather
# &text=94070 <- this will be the payload
# &response_url=https://hooks.slack.com/commands/1234/5678
# &trigger_id=13xxxxxxx09.73xxxx920.8xxxxxxxxxxx8f008e0
# &api_app_id=A123456


# We'll probably want these items:
# user_name=josh
# text=codewars+6kyu+javascript+elixir+python+200votes+10stars <- parse this
# api_app_id=os.environ.get("SLACK_APP_ID")


def extract_payload(payload):
    """Extract the form encoded data from slack into a dict.

    This also checks that it was sent by the correct (our) slack app.
    """
    data = parse_qs(payload)
    if data["api_app_id"][0] == environ.get("SLACK_APP_ID"):
        print("extracting payload")
        result = {
            "user_id": safe_list_get(data.get("user_id", None), 0, None),
            "user_name": safe_list_get(data.get("user_name", None), 0, None),
            "text": safe_list_get(data.get("text", None), 0, None),
            "response_url": safe_list_get(data.get("response_url", None), 0, None),
            "channel_name": safe_list_get(data.get("channel_name", None), 0, None),
            "channel_id": safe_list_get(data.get("channel_id", None), 0, None),
            "command": safe_list_get(data.get("command", None), 0, None),
        }
        print("result is", result)
        return result
    else:
        print(f"the payload has the wrong app id: {data['api_app_id']}")
        return None


def raw_text_to_query(text):
    """Turns the `text` field of a Slack message into a query."""
    if not text:
        print("raw_text_to_query didn't get `text`", text)
        return None

    # extract words and remove empty spaces
    words = [w.strip().lower() for w in text.split(" ") if w.strip()]
    print("words", words)
    # TODO: if the first word is "help" then it should return help information

    # figure out what kind of mongo query should be generated
    sites = [
        "codewars",
        # TODO enable these
        # "projecteuler",
        # "leetcode",
    ]
    site = None
    for s in sites:
        if s in words:
            site = s

    print("site is", site)

    if site == "codewars":
        return _generate_codewars_query(words)
    # elif site == "leetcode":
    #     return _generate_leetcode_query(words)
    # elif site == "projecteuler":
    #     return _generate_projecteuler_query(words)

    return None


def _generate_codewars_query(words):
    """Generates a mongo query based on the text."""
    # these were extracted from the mongo database
    # it's a dict for faster lookup
    query = {"source": "codewars", "languages": []}
    pattern = re.compile(r"^(\d{1,})(kyu|votes?|stars?)$")

    for w in words:
        m = re.match(pattern, w)
        if m:
            # example:
            # level: "6", key: "kyu"
            level, key = m.groups()
            query[key] = int(level)
        else:
            language_choice = codewars_valid_languages.get(w, None)
            if language_choice:
                query["languages"].append(language_choice)

    print("generated query", query)
    return query
