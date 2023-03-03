"""
Module to compute the sum of all the unique multiples of particular
numbers up to but not including that number.
"""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Calculates the sum of all the unique multiples of the numbers
    in multiples up to but not including limit.
    
    1. The function uses a set comprehension to generate a set of
       all the multiples of the given numbers.
    2. The comprehension iterates over each number "base" in the multiples
       argument, checking that base is not zero (the if base condition).
       If base is zero, it would lead to an infinite loop and an error.
    3. For each valid base, the comprehension generates a range object using
       the range() function.
       The range object starts at base and goes up to, but not including,
       the limit argument, with a step of base. This generates all the
       multiples of base up to the limit.
    4. The set comprehension gathers all the multiples of the numbers into a
       set. The use of set ensures that each multiple is unique, even if it is
       a multiple of multiple numbers.
    5. Finally, the function returns the sum of all the multiples in the set
       using the built-in sum() function.

    Args:
        limit (int): The limit below which multiples are summed.
        multiples (list[int]): The numbers whose multiples should be summed.

    Returns:
        int: The sum of the unique multiples.
    """
    return sum({
        n
        for base in multiples if base
        for n in range(base, limit, base)
    })
