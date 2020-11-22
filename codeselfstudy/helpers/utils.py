"""Utility functions."""
import re
import secrets
from uuid import uuid4
from urllib.parse import urlparse

import bleach
from bs4 import BeautifulSoup
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


def clean_user_input(content):
    """
    Bleach the input and make sure it's safe.

    This allows loading images, but only if they are locally hosted on the
    same domain.
    """
    bleached = bleach.clean(
        content,
        strip=True,
        tags=["a", "abbr", "acronym", "b", "blockquote", "code", "em", "i", "img", "li", "ol", "strong", "ul"],
        attributes={"img": ["src"]}
    )

    # Just to make sure no images are loaded from anywhere other than approved
    # sites.
    soup = BeautifulSoup(bleached)
    imgs = soup.select("img")
    allowed_image_hosts = [
        "codeselfstudy.com",
        "localhost",
    ]

    for img in imgs:
        parsed_url = urlparse(img["src"])
        if parsed_url.netloc and parsed_url.netloc not in allowed_image_hosts:
            # delete the element
            img.decompose()


def cook_markdown(md):
    """
    Safely turn markdown into HTML.
    """
    cleaned = clean_user_input(md)
    html = markdown(cleaned, extensions=["fenced_code", "tables"])
    return html


def fix_project_euler_relative_paths(raw_description):
    """
    Change the relative URLs in `img` tags to absolute URLs.
    """
    # TODO: put the images here:
    base_url = "/static/projecteuler/"
    soup = BeautifulSoup(raw_description, "html.parser")
    imgs = soup.select("img")
    pattern = re.compile(r"^http.+")

    for img in imgs:
        if not pattern.match(img["src"]):
            img["src"] = f"{base_url}{img['src']}"

    return str(str(soup))
