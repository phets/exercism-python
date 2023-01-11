def steps(number: int) -> int:
    if not ( isinstance(number, int) and number > 0 ):
        raise ValueError('Only positive integers are allowed')
    steps = 0
    while number != 1:
        number = do_step(number)
        steps += 1
    return steps

def do_step(number: int) -> int:
    if number % 2 == 0:
        return number / 2
    return 3 * number + 1
