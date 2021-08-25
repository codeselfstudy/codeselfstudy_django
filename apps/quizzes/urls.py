from django.urls import path

from . import views

app_name = "quizzes"

urlpatterns = [
    path("<int:quiz_id>", views.quiz, name="quiz"),
]
