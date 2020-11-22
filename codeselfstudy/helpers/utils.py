"""Utility functions."""
import secrets
from uuid import uuid4

import bleach
from markdown import markdown
# markdown has a codehilite extension that can be enabled. If we want to try it, the docs are here:
# https://python-markdown.github.io/extensions/code_hilite/
# Another option is to do the syntax highlighting on the frontend.
from markdown.extensions import fenced_code, tables  # type: ignore  # noqa: F401
from django.template.defaultfilters import slugify


def safe_list_get(lst, idx, default):
    """
    Safely get a list element without risking an error.

    >>> safe_list_get([1, 2, 3], 0, None)
    1
    >>> safe_list_get([1, 2, 3], 10, None)
    None
    >>> safe_list_get([], 3, None)
    None
    """
    if not lst:
        return default

    try:
        return lst[idx]
    except IndexError:
        return default


def create_random_slug():
    """
    Create a random slug.
    """
    s = str(uuid4()).split("-")[0]
    return slugify(s)


def create_entity_id(num_bytes: int):
    """Generate a random, secure string of the given length _in bytes_ (not
    chars).

    Example output with 16 bytes:
    "0hBJj83LDfPs0VlhMhkGuw"

    Example output with 32 bytes:
    "l9qR1wvRiM6HfS86gBV79EM9Plb5Z0s8eshFXo6nHhs"
    """
    return secrets.token_urlsafe(num_bytes)


def cook_markdown(md):
    """
    Bleach the input and turn markdown into HTML.

    By default, bleach allows these tags:
    ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul']
    """
    bleached = bleach.clean(md, strip=True)
    html = markdown(bleached, extensions=["fenced_code", "tables"])
    return html
