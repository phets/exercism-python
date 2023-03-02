"""
Module to calculate the "Hamming distance" between two strands of DNA.
"""

def distance(strand_a: str, strand_b: str) -> int:
    """Calculates the Hamming distance between two strands of DNA.

    Args:
        strand_a (str): String representing the first strand in the format "CGATATCA"
        strand_b (str): String representing the second strand in the format "CGATATCA"

    Raises:
        ValueError: Exception in case the two strands are not of equal length

    Returns:
        int: The Hamming distance between the two strands.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum( base_a != base_b for base_a, base_b in zip(strand_a, strand_b))

