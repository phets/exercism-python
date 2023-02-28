def largest(min_factor: int=0, max_factor: int=0) -> tuple:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validate(min_factor, max_factor)

    largest_palindrome = 0
    largest_palindrome_factors = []
    for product in range (min_factor ** 2, max_factor ** 2 + 1):
        if is_palindrome(product) and product > largest_palindrome:
            factors = find_factors(product, min_factor, max_factor)
            if not factors:
                continue
            else:
                largest_palindrome = product
                largest_palindrome_factors = factors
    if not largest_palindrome_factors:
        return (None,[])
    else:
        return (largest_palindrome, largest_palindrome_factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validate(min_factor, max_factor)

    smallest_palindrome =  max_factor ** 2
    smallest_palindrome_factors = []
    for product in range (min_factor ** 2, max_factor ** 2 + 1):
        if is_palindrome(product) and product < smallest_palindrome:
            factors = find_factors(product, min_factor, max_factor)
            if not factors:
                continue
            else:
                smallest_palindrome = product
                smallest_palindrome_factors = factors
    if not smallest_palindrome_factors:
        return (None,[])
    else:
        return (smallest_palindrome, smallest_palindrome_factors)


def is_palindrome(number):
    return str(number) == str(number)[::-1]

def validate(min_factor: int, max_factor: int) -> None:
    if min_factor < max_factor: raise ValueError("min must be <= max")

def find_factors(number: int, min_factor: int, max_factor: int) -> list:
    output = []
    for factor_1 in range(min_factor,max_factor+1,1):
        for factor_2 in range(min_factor,max_factor+1,1):
            if factor_1 * factor_2 == number:
                output.append([factor_1, factor_2])
    return output

print(largest(15,15))
print(smallest(1002,1003))