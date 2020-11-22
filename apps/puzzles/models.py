from django.db import models
# from taggit.managers import TaggableManager

from codeselfstudy.models import CreatedUpdatedModel
from codeselfstudy.helpers.utils import create_random_slug, cook_markdown, fix_project_euler_relative_paths


class PuzzleSources(models.TextChoices):
    """
    The site to send people to to solve the puzzle.
    """
    CODEWARS = "Codewars", "Codewars"
    LEETCODE = "Leetcode", "Leetcode"
    PROJECT_EULER = "Project Euler", "Project Euler"
    CODESELFSTUDY = "Code Self Study", "Code Self Study"
    UNKNOWN = "Unknown", "Unknown"


class DifficultyLevel(models.IntegerChoices):
    """
    This is our own ranking system.

    1 is the easiest, 10 is the hardest. Maybe it could be shown visually
    on a bar with green, yellow, and red gradient kind of like this:
    https://tinkersphere.com/4740-large_default/led-bar-graph-red-yellow-green.jpg

    Codewars has 8 levels with 1 being the hardest. Leetcode has hard,
    medium, and easy. I think Hackerrank has: easy, intermediate, hard,
    expert, advanced. Project Euler apparently has 20 difficulty levels.
    Those could be mapped to our ranking system.
    """
    LEVEL_UNKNOWN = 0
    LEVEL_ONE = 1  # easiest
    LEVEL_TWO = 2
    LEVEL_THREE = 3
    LEVEL_FOUR = 4
    LEVEL_FIVE = 5
    LEVEL_SIX = 6
    LEVEL_SEVEN = 7
    LEVEL_EIGHT = 8
    LEVEL_NINE = 9
    LEVEL_TEN = 10  # hardest


class Puzzle(CreatedUpdatedModel):

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    source = models.CharField(
        max_length=100,
        choices=PuzzleSources.choices,
        default=PuzzleSources.UNKNOWN,
    )

    difficulty = models.IntegerField(
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.LEVEL_UNKNOWN
    )

    # TODO: Don't display this anywhere because it's raw user input.
    unsafe_description = models.TextField()

    # TODO: It should be bleached and cooked on save.
    cooked_description = models.TextField(help_text="The description of the puzzle")

    # TODO add a unique slug (not a "friendly-URL")
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
    # a dump of the original data
    original_raw_data = models.JSONField(
        blank=True,
        default=dict,
        help_text="Any Python data type here will be turned into JSONB.",
    )

    # Warning: tags won't be saved when doing `commit=False` unless you do
    # `.save_m2m()`. See the following link.
    # https://django-taggit.readthedocs.io/en/latest/forms.html
    # When adding tags, we can downcase them all to keep things simple.
    # TODO: I removed tags for now, because it isn't needed in the first version
    # tags = TaggableManager()

    # TODO: enable this after the model is stable
    # history = HistoricalRecords()

    def save(self, *args, **kwargs):
        """
        Cook the markdown when it's saved.

        (The slug is handled above.)
        """
        if self.source == PuzzleSources.PROJECT_EULER:
            description = fix_project_euler_relative_paths(self.unsafe_description)
        else:
            description = self.unsafe_description
        self.cooked_description = cook_markdown(description)
        return super(Puzzle, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
