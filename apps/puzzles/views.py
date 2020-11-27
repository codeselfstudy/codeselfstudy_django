# from django.shortcuts import render
from django.http import JsonResponse


def slack_slash_command(request):
    payload = {
        "hello": "slack",
    }
    return JsonResponse(payload)
