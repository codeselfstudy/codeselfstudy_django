"""
This module contains code that handles requests for puzzles.

For example, the `slack` app in this repo will send this file some JSON and
this file will return a puzzle to the caller.
"""
import logging
from typing import Dict

from .models import Puzzle
from .helpers import source_string_to_puzzle_source, difficult_int_to_puzzle_difficulty

log = logging.getLogger(__name__)


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


def _source_command_to_puzzle_response(q):
    log.info(f"source command query: {q}")

    source = source_string_to_puzzle_source(q.get("source"))
    difficulty = difficult_int_to_puzzle_difficulty(q.get("difficulty"))

    # TODO: add languages to the Django query below.
    # The `q` query will be a dictionary with a `languages` key that holds an array.
    # The structure of that data is in Postgres and an example raw SQL query would be:
    #     SELECT original_raw_data ->> 'languages'
    #     FROM puzzles_puzzle
    #     WHERE source='Codewars'
    #     LIMIT 1;
    # See https://github.com/codeselfstudy/codeselfstudy_django/issues/18

    # There may be a better way to make this query.
    puzzles = Puzzle.objects.filter(
        source=source,
        was_seen=False,
        difficulty=difficulty,
    )[:1]
    puzzle = puzzles[0]
    return puzzle
