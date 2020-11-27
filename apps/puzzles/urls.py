from django.urls import path

from . import views

app_name = "puzzles"

# The URLs can get more interesting later, but the first step is to recreate
# the behavior from the Flask app. These differ from the Flask URLs by being
# prefixed with `api`. It's a temporary way to avoid using routes that might be
# used for web ingerfaces later.
urlpatterns = [
    path("slack/", views.slack_slash_command, name="slack_slash_command"),
]
