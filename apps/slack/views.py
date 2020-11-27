from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def puzzle_slash_command(request):
    if request.method != "POST":
        raise Http404("Not found")

    payload = {
        "hello": "slack",
    }
    return JsonResponse(payload)
