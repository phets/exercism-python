def is_triangle(fn):
    def inner(sides):
        has_three_sides = len(sides) == 3
        return sum(sides) > 2 * max(sides) and has_three_sides and fn(sides) 
    return inner
    
# The @ decorator passes the euilateral function defined just below as the fn argument 
# into the is_triangle function and assigns the output of is_triangle (the inner function)
# to equilateral.
@is_triangle
def equilateral(sides):
    # A set only holds unique elements.
    # When the elements of the sides array are all equal the set reduces
    # to a single unique element making its length == 1.
    return len(set(sides)) == 1

@is_triangle
def isosceles(sides):
    # When there are at least two equal elements of the sides array
    # it means that the triangle is either 
    # isosceles [len(set(sides)) == 2] or
    # equilateral [len(set(sides)) == 1].
    return len(set(sides)) < 3

@is_triangle
def scalene(sides):
    return len(set(sides)) == 3
