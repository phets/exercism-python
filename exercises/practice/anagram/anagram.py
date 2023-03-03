"""
Module to solve the anagram exercise from exercism.org.
"""

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Selects the entries in the candidates list that are anagrams
    of word.

    Args:
        word (str): The word for which the candidates must be an anagram.
        candidates (list[str]): The list of anagram candidates.

    Returns:
        list[str]: The anagrams of word included in the candidates list.
    """
    return [
        anagram
        for anagram in candidates
        if anagram.lower().strip() != word.lower().strip()
        and sorted(anagram.lower().strip()) == sorted(word.lower().strip())
    ]
