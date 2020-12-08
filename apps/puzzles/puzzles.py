"""
This module contains code that handles requests for puzzles.

For example, the `slack` app in this repo will send this file some JSON and
this file will return a puzzle to the caller.
"""
from typing import Dict


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
