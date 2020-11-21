"""
This module contains base modules that apps can use.
"""
from django.db import models


class CreatedUpdatedModel(models.Model):
    """This is an abstract class that other classes can use

    It adds `created_at` and `updated_at` fields.

    I followed these blog posts:
    https://www.dothedev.com/blog/django-created-at-updated-at-auto-fields/
    https://medium.com/@adriennedomingus/djangos-auto-now-and-auto-now-add-fields-for-auditing-creation-and-modification-timestamps-ed73e1dbe9d1
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
