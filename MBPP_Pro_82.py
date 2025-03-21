import math

def circle_circumference(r):
    return 2 * math.pi * r

def total_circumference(radii):
    total = 0
    for r in radii:
        total += circle_circumference(r)
    return total
