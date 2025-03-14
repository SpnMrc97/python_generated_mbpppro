import math

def total_circumference(radii):
    """
    Calculate the total circumference of multiple circles based on their radii.

    Parameters:
    radii (list of float): A list of radii of the circles.

    Returns:
    float: The total circumference of all circles combined.
    """
    total = 0
    for radius in radii:
        circumference = 2 * math.pi * radius
        total += circumference
    return total
