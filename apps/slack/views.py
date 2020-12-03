import logging
from random import choice
from textwrap import dedent

from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .signature import verify_signature
from puzzles.models import Puzzle

log = logging.getLogger(__name__)


@csrf_exempt
def puzzle_slash_command(request):
    if request.method != "POST":
        raise Http404("Not found")

    slack_signature = request.headers.get("X-Slack-Signature")
    slack_ts = request.headers.get("X-Slack-Request-Timestamp")

    data = request.body.decode("utf-8")

    if not verify_signature(slack_signature, slack_ts, data):
        return HttpResponse('Unauthorized', status=401)

    # get a random puzzle, medium difficulty
    pks = Puzzle.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    # p = Puzzle.objects.order_by("?").get(difficulty=3)[0]
    p = Puzzle.objects.get(pk=random_pk)

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
    body = dedent(f"""
    Try solving this random programming puzzle. (Tip: run the command again if you want to load a different one.)

    *{p.title}* (difficulty: {difficulty_names[p.difficulty]})
    {p.original_url}
    """)

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
