"""
This module solves the two_fer exercise from exercism.org.

Functions:

    two_fer(str) -> str
"""

def two_fer(name: str='you') -> str:
    """
    This function creates and returns a string like:
    One for {name}, one for me.

    Args:
        name (str, optional): The name to insert in the string. Defaults to 'you'.

    Returns:
        str: One for {name}, one for me.
    """
    return f'One for {name}, one for me.'
