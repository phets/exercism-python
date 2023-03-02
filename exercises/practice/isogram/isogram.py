"""
Module to find isogram strings.
An isogram (also known as a "non-pattern word") is a word
or phrase without a repeating letter, however spaces and
hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
"""

def is_isogram(phrase: str) -> bool:
    """
    Determines if the input phrase is an isogram.

    Args:
        phrase (str): The string to be checked.

    Returns:
        bool: True if the input is an isogram.
    """
    phrase_only_alnum = ''.join(filter(str.isalnum, phrase.strip().lower()))
    return len(set(phrase_only_alnum)) == len(phrase_only_alnum)
