"""
Useful functions for formatting text.
"""
import os
from textwrap import dedent


def format_slack_error_message():
    """This is the message that gets sent back to Slack when there is an error."""
    return dedent("""
        Your query wasn't formatted correctly or there was another error. Try typing something like this:

        ```/puzzle codewars js python elixir 5kyu 100votes```

        Parameters can look like this:
        - *source:* `codewars` (required)
        - *languages:* `python js fortran c` (optional)
        - *difficulty:* `5kyu` (optional)
        - *minimum votes:* `100votes` (optional)
        - *minimum stars:* `100stars` (optional)

        *Tip:* if you want to encourage people to join you, form the query with some popular languages like `javascript python elixir` to increase interest in solving the puzzle. If you want to contribute to the development of this app, join the #engine-room channel.
    """)
