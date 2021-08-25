from django.shortcuts import render, get_object_or_404

from .models import Quiz


def list(request):
    quizzes = Quiz.objects.all()
    context = {
        "quizzes": quizzes
    }
    return render(request, "quizzes/list.html", context)


def quiz(request, quiz_id):
    q = get_object_or_404(Quiz, pk=1)
    context = {
        "quiz": q,
    }
    return render(request, "quizzes/detail.html", context)
