"""
Module to solve the etl exercise from exercism.org.
"""

def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Transform the scrabble scoring data from the legacy format
    to the new format.

    Args:
        legacy_data (dict[int, list[str]]): Scrabble scoring data
        in the form {1: ["A", "E"], 2: ["D", "G"]}

    Returns:
        dict[str, int]: Scrabble scoring data in the new form
        {"a": 1, "d": 2, "e": 1, "g": 2}
    """
    return {
        letter.lower(): score 
        for score in legacy_data 
        for letter in legacy_data[score]
    }
