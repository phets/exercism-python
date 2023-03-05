def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")
    if sum(find_factors(number)) < number:
        return "deficient"
    if sum(find_factors(number)) == number:
        return "perfect"
    if sum(find_factors(number)) > number:
        return "abundant"

def find_factors(number: int) -> list[int]:
    if number < 1:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")
    return [factor for factor in range(1, number//2 + 1) if number % factor == 0 ]
