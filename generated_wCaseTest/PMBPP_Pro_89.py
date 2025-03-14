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

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_circumference([1, 2, 3]) == 2 * math.pi * (1 + 2 + 3)
assert total_circumference([0, 0, 0]) == 0
assert total_circumference([5]) == 2 * math.pi * 5

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)