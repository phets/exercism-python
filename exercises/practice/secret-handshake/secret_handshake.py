"""
Module to solve the secret handshake exercise from exercism.org.
https://exercism.org/tracks/python/exercises/secret-handshake
"""
events = ['wink', 'double blink', 'close your eyes', 'jump']

def commands(binary_str: str) -> list[str]:
    """
    Calculates the event sequence for the secret handshake by:
    1. Converting the string into an integer.
    2. Using binary logic (&) and shift (<<) operators to determine the events.

    Args:
        binary_str (str): A string representing a binary number.
        The string must have 5 digits e.g. "10010".

    Returns:
        list[str]: The sequence of events for the secret handshake.
    """
    int_code = int(binary_str.strip(), 2)
    out = [j for i,j in enumerate(events) if int_code & 1 << i]
    if int_code & 1 << 4:
        out.reverse()
    return out
