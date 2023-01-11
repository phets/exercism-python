# An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
#
# For example:
#
# 9 is an Armstrong number, because 9 = 9^1 = 9
# 10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
# 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

def is_armstrong_number(number):
    # Exclude negative and decimal numbers since they cannot be Armstrong numbers.
    if number < 0 or not isinstance(number, int):
        raise ValueError("is_armstrong_number function only accepts positive integers.")
    # Get the number of digits by casting number as a string and counting the characters.
    # Math.log10 doesn't work because it fails with 0 - ValueError: math domain error.
    number_of_digits = len(str(number))
    # Extract the single digits into an array
    # by treating "number" as a string, looping over each character,
    # and casting it back as an integer.
    list_of_digits = [int(i) for i in str(number)]
    # Execute i**number_of_digits on each element of the list_of_digits
    # array using list comprehension and sum the results.
    calculated = sum(i ** number_of_digits for i in list_of_digits)
    return calculated == number
