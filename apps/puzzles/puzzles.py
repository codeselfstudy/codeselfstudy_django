"""
This module contains code that handles requests for puzzles.

For example, the `slack` app in this repo will send this file some JSON and
this file will return a puzzle to the caller.
"""
from typing import Dict

from .models import Puzzle


def query_to_puzzle(q: Dict):
    """
    Takes a query in the form of a dict returned by a "source command" or a
    "url command", and returns a puzzle.

    This is from an example source command:
    ```
    {'difficulty': 3,
    'languages': ['python', 'js', 'raku', 'fortran'],
    'source': 'codewars'}
    ```

    This is from an example url command:
    ```
    {'url': 'https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/'}
    ```
    """

    # TODO: query a puzzle here based on the command

    if q.get("url") is not None:
        # it's a url command
        return _url_command_to_puzzle_response(q)
    else:
        # it's a source command
        return _source_command_to_puzzle_response(q)


def _url_command_to_puzzle_response(q: Dict):
    # TODO: check that it's a valid puzzle URL, then return it
    pass


def _source_command_to_puzzle_response(q: Dict):
    # TODO: get a puzzle from the database
    pass
