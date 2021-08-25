from django.db import models
from codeselfstudy.models import CreatedUpdatedModel


class Quiz(CreatedUpdatedModel):
    title = models.CharField(
        max_length=255,
        help_text="The title of the quiz",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizzes"


class Question(CreatedUpdatedModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body[:25]


class Choice(CreatedUpdatedModel):
    text = models.CharField(
        max_length=255
    )
    is_correct = models.BooleanField(
        default=False,
        help_text="Is this the correct answer? Only one choice can be correct."
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
