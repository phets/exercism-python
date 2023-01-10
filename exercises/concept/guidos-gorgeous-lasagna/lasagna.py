"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

    pass


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - The number of layers of the lasagna.
    :return: int - preparation time, derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of the desired lasagna as
    an argument and returns how many minutes it will take to prepare the lasagna.
    Calculated by number_of_layers * PREPARATION_TIME.
    """

    return number_of_layers * PREPARATION_TIME
# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the time that has been spent preparing and cooking the lasagna.

    :param number_of_layers: int - The number of layers of the lasagna.
    :param elapsed_bake_time: int - The number of minutes the lasagna has been cooking in the oven.
    :return: int - The number of minutes that have been spent preparing and cooking the lasagna.

    Function that takes the number of layers of the lasagna and the time that
    the lasagna has been cooking in the oven and returns the total number of
    minutes that have been spent preparing and cooking the lasagna.
    Calculated by preparation_time_in_minutes(number_of_layers) + elapsed_bake_time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time