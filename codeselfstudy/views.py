"""
Custom error pages.
"""
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

log = logging.getLogger(__name__)


def not_found(request, exception):
    """Handle 404."""
    return render(request, "global/errors/404.html", status=404)


def server_error(request):
    """Handle 500."""
    return render(request, "global/errors/500.html", status=500)


# def bad_request(request):
#     """Handle 400."""
#     return render(request, "global/errors/400.html", status=400)


# def denied(request):
#     """Handle 403."""
#     return render(request, "global/errors/403.html", status=403)

@require_GET
def robots_txt(request):
    """
    Programatically generate robots.txt rules here.
    """
    lines = [
        "User-Agent: *",
        "Disallow: /whatever/",
        # "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
