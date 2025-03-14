def total_square_perimeter(side_lengths):
    """
    Calculate the total perimeter of all squares given their side lengths.

    Parameters:
    side_lengths (list of int): A list containing the side lengths of squares.

    Returns:
    int: The total perimeter of all the squares.
    """
    total_perimeter = 0
    for side in side_lengths:
        # Perimeter of a square is 4 times the side length
        total_perimeter += 4 * side
    return total_perimeter

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_square_perimeter([1, 2, 3]) == 24
assert total_square_perimeter([0, 10, 20]) == 120
assert total_square_perimeter([]) == 0
assert total_square_perimeter([5]) == 20

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)