"""
Module to flatten an arbitrarily nested list and remove None values.
"""

def flatten(iterable: list) -> list:
    """
    Recursive function to flatten a nested list.
    The nesting can be arbitrarily deep.
    When the list is flat None values are removed.

    Args:
        iterable (list): The list to flatten.

    Returns:
        list: The flattened list.
    """
    out = []
    for item in iterable:
        if isinstance(item, list):
            out.extend(flatten(item))
        elif item is not None:
            out.append(item)
    return out


