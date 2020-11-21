from django.db import models
from taggit.managers import TaggableManager

from codeselfstudy.models import CreatedUpdatedModel
from codeselfstudy.helpers.utils import create_random_slug


class Puzzle(CreatedUpdatedModel):

    class PuzzleSources(models.TextChoices):
        CODEWARS = "Codewars", "Codewars"
        LEETCODE = "Leetcode", "Leetcode"
        PROJECT_EULER = "Project Euler", "Project Euler"
        CODESELFSTUDY = "Code Self Study", "Code Self Study"
        UNKNOWN = "Unknown", "Unknown"

    class DifficultyLevel(models.IntegerChoices):
        """
        1 is the easiest, 10 is the hardest. Maybe it could be shown visually
        on a bar with green, yellow, and red gradient kind of like this:
        https://tinkersphere.com/4740-large_default/led-bar-graph-red-yellow-green.jpg

        Codewars has 8 levels with 1 being the hardest. Leetcode has hard,
        medium, and easy. I think Hackerrank has: easy, intermediate, hard,
        expert, advanced. Project Euler apparently has 20 difficulty levels.
        """
        UNKNOWN = 0
        ONE = 1  # easiest
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10  # hardest

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    source = models.CharField(
        choices=PuzzleSources.choices,
        default=PuzzleSources.UNKNOWN,
    )

    difficulty = models.IntegerField(
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.UNKNOWN
    )

    # TODO: Don't display this anywhere because it comes from the Internet.
    unsafe_html = models.TextField()

    # TODO: It should be bleached and cooked on save.
    cooked_html = models.TextField(help_text="The description of the puzzle")

    # TODO add a unique, unguessable slug
    slug = models.SlugField(
        default=create_random_slug,
        max_length=255,
    )

    # The `original_*` fields here come from external sites, if applicable
    original_url = models.URLField(
        null=True,
        blank=True,
        help_text="If the puzzle originated somewhere else, put the full URL here"
    )
    original_votes = models.IntegerField(null=True, blank=True)
    original_stars = models.IntegerField(null=True, blank=True)
    original_unsafe_html = models.TextField(null=True, blank=True)

    # Warning: tags won't be saved when doing `commit=False` unless you do
    # `.save_m2m()`. See the following link.
    # https://django-taggit.readthedocs.io/en/latest/forms.html
    # When adding tags, we can downcase them all to keep things simple.
    tags = TaggableManager()
    # category = TODO ? or is this even needed?

    # TODO: enable this
    # history = HistoricalRecords()
