from .models import PuzzleSources, DifficultyLevel


def source_string_to_puzzle_source(source_string):
    """
    This converts a string like "codewars" to a format the the Puzzle model understands.

    "codewars" will become "Codewars", but this uses the actual PuzzleSources
    class instead of hard-coded strings, in case something changes later.
    """
    if source_string == "codewars":
        source = PuzzleSources.CODEWARS
    elif source_string == "leetcode":
        source = PuzzleSources.LEETCODE
    elif source_string == "projecteuler":
        source = PuzzleSources.PROJECTEULER
    elif source_string == "codeselfstudy":
        source = PuzzleSources.CODESELFSTUDY
    else:
        # put some default here
        source = PuzzleSources.CODWARS

    return source


def difficult_int_to_puzzle_difficulty(difficulty_int):
    """
    Converts the difficulty int from the query into one that the Puzzle model
    can understand.
    """
    if difficulty_int == 1:
        difficulty = DifficultyLevel.LEVEL_ONE
    elif difficulty_int == 2:
        difficulty = DifficultyLevel.LEVEL_TWO
    elif difficulty_int == 3:
        difficulty = DifficultyLevel.LEVEL_THREE
    elif difficulty_int == 4:
        difficulty = DifficultyLevel.LEVEL_FOUR
    else:
        difficulty = DifficultyLevel.LEVEL_UNKNOWN

    return difficulty
