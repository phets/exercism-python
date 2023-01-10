def square(number):
    # when the square value is not in the acceptable range
    if(number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")

    # With bit-shift operator
    # return 1 << (number - 1)
    return 2 ** (number - 1)


def total():
    total_grains = 0

    for cell in range(1,65):
        total_grains += square(cell)
    
    # With bit-shift operator
    # return ( 1 << 64 ) - 1
    return total_grains
