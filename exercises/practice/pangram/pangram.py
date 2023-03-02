"""
Module to find whether a string is a pangram.
"""

import string

def is_pangram(sentence: str) -> bool:
    """
    Function that determines if an input string is a pangram.
    A pangram is a sentence that contains all the letters of the alphabet.

    Args:
        sentence (str): The sentence to be analyzed.

    Returns:
        bool: True if the sentence is a pangram.
    """
    if sentence.strip() == '':
        return False
    input_set = set(sentence.strip().lower())
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(input_set)
