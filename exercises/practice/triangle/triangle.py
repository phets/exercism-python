def is_triangle(sides):
    sides.sort()
    if 0 > len(sides) > 3 :
        raise ValueError("Sides must be an array containing exactly 3 elements.")
        return False
    if sides[0] + sides[1] <= sides[2] :
        return False
    return True

def equilateral(sides):
    if not is_triangle(sides) :
        return False
    if sides[0] == sides[1] == sides[2] :
        return True
    return False


def isosceles(sides):
    if not is_triangle(sides) :
        return False
    if equilateral(sides) :
        return True
    if sides[0] == sides[1] != sides[2] :
        return True
    if sides[1] == sides[2] != sides[0] :
        return True
    if sides[0] == sides[2] != sides[1] :
        return True
    return False


def scalene(sides):
    if not is_triangle(sides) :
        return False
    if sides[0] != sides[1] != sides[2] :
        return True
    return False
