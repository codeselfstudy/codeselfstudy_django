import logging

# from random import choice
from textwrap import dedent

from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .signature import verify_signature
from .helpers import is_valid_slack_app, extract_slack_payload, parse_command

# from puzzles.models import Puzzle
from puzzles.puzzles import query_to_puzzle
from codeselfstudy.settings import DEBUG

log = logging.getLogger(__name__)


@csrf_exempt
def puzzle_slash_command(request):
    if request.method != "POST":
        log.error(
            f"request to puzzle_slash_command was not a POST. Headers: {request.headers}"
        )
        raise Http404("Not found")

    slack_signature = request.headers.get("X-Slack-Signature")
    slack_ts = request.headers.get("X-Slack-Request-Timestamp")

    data = request.body.decode("utf-8")

    # only check for Slack signatures in production
    if DEBUG is False and (
        not verify_signature(slack_signature, slack_ts, data)
        or not is_valid_slack_app(data)
    ):
        log.error(
            f"request was POST but not valid: {request.headers} /// {request.body}"
        )
        return HttpResponse("Unauthorized", status=401)

    slack_payload = extract_slack_payload(data)
    command = slack_payload.get("text")
    log.info(f"slack_payload: {slack_payload}")

    q = parse_command(command)
    p = query_to_puzzle(q)

    # Mark the puzzle as seen so that it doesn't show up again.
    p.was_seen = True
    p.save()
    log.info(f"the saved puzzle is: {p.__dict__}")

    # TODO: fix this quick, tmp hack
    difficulty_names = {
        0: "unknown",
        1: "novice",
        2: "easy",
        3: "medium",
        4: "hard",
    }

    # TODO: parse the `data` and figure out what command to send back
    # If can parse the query and find a puzzle in the database, send it back.
    body = dedent(
        f"""
    Try solving this random programming puzzle. (Tip: run the command again if you want to load a different one.)

    *{p.title}* (difficulty: {difficulty_names[p.difficulty]})
    {p.original_url}
    """
    )

    # TODO: get formatting ideas from https://api.slack.com/block-kit
    payload = {
        # TODO: if the request isn't successful, send the error message back but NOT in_channel.
        "response_type": "in_channel",
        # "response_type": "ephemeral",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": body,
                },
            },
            # {
            #     "type": "header",
            #     "text": {
            #         "type": "plain_text",
            #         "text": header_text,
            #         "emoji": True,
            #     },
            # },
            # {
            #     "type": "section",
            #     "text": {
            #         "type": "mrkdwn",
            #         "text": url_text,
            #     },
            # },
        ],
    }

    return JsonResponse(payload)
