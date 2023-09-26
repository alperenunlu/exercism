def equilateral(sides):
    triangle_sum = sum(sides)
    for side in sides:
        if side == 0 or side > triangle_sum - side:
            return False
        
    return len(set(sides)) == 1


def isosceles(sides):
    triangle_sum = sum(sides)
    for side in sides:
        if side == 0 or side > triangle_sum - side:
            return False
        
    return len(set(sides)) <= 2


def scalene(sides):
    triangle_sum = sum(sides)
    for side in sides:
        if side == 0 or side > triangle_sum - side:
            return False
        
    return len(set(sides)) == 3

