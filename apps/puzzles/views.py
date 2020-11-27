# from django.shortcuts import render
from django.http import JsonResponse


def random_puzzle(request):
    payload = {
        "hello": "world",
    }
    return JsonResponse(payload)


def random_puzzle_by_source(request, source):
    payload = {
        "source": source,
    }
    return JsonResponse(payload)


# TODO: I don't know if this is needed. People will submit queries or URLs but
# probably not IDs, since they can paste the entire URL.
# def puzzle_by_id(request, puzzle_id):
#     payload = {
#         "puzzle": puzzle_id,
#     }
#     return JsonResponse(payload)


def slack_slash_command(request):
    payload = {
        "hello": "slack",
    }
    return JsonResponse(payload)
