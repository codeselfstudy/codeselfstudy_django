from django.db import models

from codeselfstudy.models import CreatedUpdatedModel
from codeselfstudy.helpers.utils import create_random_slug


class Puzzle(CreatedUpdatedModel):

    class PuzzleSources(models.TextChoices):
        CODEWARS = "Codewars", "Codewars"
        LEETCODE = "Leetcode", "Leetcode"
        PROJECT_EULER = "Project Euler", "Project Euler"
        CODESELFSTUDY = "Code Self Study", "Code Self Study"
        UNKNOWN = "Unknown", "Unknown"

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    source = models.CharField(
        choices=PuzzleSources.choices,
        default=PuzzleSources.UNKNOWN,
    )

    # TODO: Don't display this anywhere.
    unsafe_html = models.TextField()

    # TODO: It should be bleached and cooked on save.
    cooked_html = models.TextField()

    # TODO add a unique, unguessable slug
    slug = models.SlugField(
        default=create_random_slug,
        max_length=255,
    )

    # history = HistoricalRecords()

    # TODO: figure out what fields we want in the Puzzle model.
    # category, tags, difficulty level, etc.
