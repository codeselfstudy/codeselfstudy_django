"""
The languages might be used in more than one part of the site, so they are in
their own app.

After more thought, we don't need this in the database right away, because it
can be pulled out of the JSONB.
"""
from django.db import models

from codeselfstudy.models import CreatedUpdatedModel


class Language(CreatedUpdatedModel):
    """
    Represents the official name of a language.
    """
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(
        help_text="Some markdown text about the language for its description page.",
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name


# TODO: figure out if this is the right way to do it.
class LanguageVariantName(CreatedUpdatedModel):
    """
    Represents a variant name of a programming language. One language has
    many variant names.

    These are the names that the language can be referred to. For example,
    c++ and cpp both refer to the same language. Perl6, Perl 6, and Raku all
    refer to the same language.
    """
    variant_name = models.CharField(unique=True, max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.variant_name
