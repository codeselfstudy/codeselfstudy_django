from django.urls import path

from . import views

app_name = "slack"

urlpatterns = [
    path("puzzles/", views.puzzle_slash_command, name="puzzle_slash_command"),
]
