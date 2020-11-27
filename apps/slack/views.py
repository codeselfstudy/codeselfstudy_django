import logging

from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .signature import verify_signature

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

    # TODO: parse the `data` and figure out what command to send back
    # If can parse the query and find a puzzle in the database, send it back.
    body = "the message that gets sent to Slack"

    # TODO: get formatting ideas from https://api.slack.com/block-kit
    payload = {
        # TODO: if the request isn't successful, send the error message back but NOT in_channel.
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": body,
                },
            },
        ],
    }

    return JsonResponse(payload)
