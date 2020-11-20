"""Utility functions."""


def safe_list_get(lst, idx, default):
    """
    Safely get a list element without risking an error.

    >>> safe_list_get([1, 2, 3], 0, None)
    1
    >>> safe_list_get([1, 2, 3], 10, None)
    None
    """
    try:
        return lst[idx]
    except IndexError:
        return default
