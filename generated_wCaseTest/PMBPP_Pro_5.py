def total_volume_cubes(side_lengths):
    """
    Calculate the total volume of multiple cubes given their side lengths.

    Parameters:
    side_lengths (list of int or float): A list containing the side lengths of the cubes.

    Returns:
    float: The total volume of all the cubes.
    """
    total_volume = 0
    for side in side_lengths:
        if side < 0:
            raise ValueError("Side length cannot be negative.")
        volume = side ** 3
        total_volume += volume
    return total_volume

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_volume_cubes([1, 2, 3]) == 36

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)