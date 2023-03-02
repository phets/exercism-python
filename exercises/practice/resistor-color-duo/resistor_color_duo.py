"""
This module solves the resistor_color_duo python exercise from exercism.org
The exercise focuses on converting resistance color codes to resistance values.

Classes:
    ResistorColors

Functions:
    value(list) -> int
"""

from enum import Enum
 
class ResistorColors(Enum):
    """
    An Enum that maps color names to resistance values.
    """
    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GREY = 8
    WHITE = 9


def value(colors: list) -> int:
    """
    A function to transform a list of colors into a two digit resistance value.
    Only the first two colors are considered, the rest are ignored.
    
    Args:
        colors (list): A list of with two or more colors.

    Returns:
        int: An integer between 1 and 99 representing the resistance value.
    """
    color1, color2, *other_colors = colors
    return int(str(ResistorColors[color1.strip().upper()].value) + str(ResistorColors[color2.strip().upper()].value))
