"""
Module to calculate dart score based on distance from centre.
"""

# math to use the math.dist function
import math

def score(x: float, y: float) -> int:
    """
    Calculates the score of a dart based on the coordinates
    where it hits.

    Args:
        x (float): x-coordinate of dart.
        y (float): y-coordinate of dart.

    Returns:
        int: The dart's score.
    """
    distance = math.dist([0,0], [x,y])
    
    if distance > 10:
        return 0
    if 10 >= distance > 5:
        return 1
    if 5 >= distance > 1:
        return 5
    if 1 >= distance:
        return 10
