"""
Useful functions for formatting text.
"""
import os
from textwrap import dedent

DISCOURSE_PUZZLES_CATEGORY = os.getenv("DISCOURSE_PUZZLES_CATEGORY")
print("puzzles category", DISCOURSE_PUZZLES_CATEGORY)

def format_codewars_puzzle_message(puzzle):
    """This formats a codewars puzzle for Slack."""
    print("helper got puzzle", puzzle)
    if not puzzle:
        return None

    languages = ", ".join(puzzle["languages"])
    # TODO: this hack could be cleaned up with the `dedent` function
    lines = [
        "Try solving this puzzle on codewars:\n",
        f"*{puzzle['name']}* ({puzzle['kyu']} kyu)",
        f"{puzzle['url']}"
        "\n",
        f"> *available in:* {languages}",
        f"> *category:* {puzzle['category']}"
    ]
    return "\n".join(lines)


def format_codewars_puzzle_for_discourse(puzzle):
    """Format a codewars puzzle to post as a forum post in Discourse."""
    print("helper got puzzle for discourse", puzzle)
    if not puzzle:
        return None

    title = f"Puzzle: {puzzle['name']} [{puzzle['category']}]"
    languages = "{}, and {}".format(", ".join(puzzle["languages"][:-1]), puzzle["languages"][-1])
    tags = ", ".join(puzzle['tags'])

    description = puzzle.get("description", None)
    if description:
        description = description.replace(r"```", "\n```\n")
    # `dedent` wasn't working for me with format strings, so I'm removing the indents manually
    lines = f""""**{puzzle["name"]}**" is a coding puzzle that people can be attempted in the following languages: {languages}.

        - **Difficulty:** {puzzle.get("kyu", "unknown")} kyu
        - **Stars:** {puzzle.get("stars", "unknown")}
        - **Votes:** {puzzle.get("votes", "unknown")}
        - **Category:** {puzzle.get("category", "unknown")}
        - **Tags:** {tags}
        - **Source:** [codewars]({puzzle["url"]})

        # Description

        {description}

        # Solve It Here

        Click the link below to solve it on Codewars:

        {puzzle["url"]}

        # Notes

        This puzzle was posted by a Slackbot via a slash command. If you want to help work on the app, send a message to @Josh.

        If you don't want to see the coding puzzles when you visit the forum, you can go into [your settings](https://forum.codeselfstudy.com/my/preferences/categories) and mute the puzzles category.
        """.split("\n")

    cleaned_lines = [line.strip() for line in lines]
    raw = "\n".join(cleaned_lines)

    return {
        "title": title,
        "raw": raw,
        "category": DISCOURSE_PUZZLES_CATEGORY
    }
