def total_pos_count(lists):
    """
    Count the number of positive numbers in multiple lists and return the total count.

    Args:
    lists (list of list of int/float): A list containing sublists of numbers.

    Returns:
    int: The total count of positive numbers across all sublists.
    """
    total_count = 0

    for sublist in lists:
        for number in sublist:
            if number > 0:
                total_count += 1

    return total_count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_pos_count([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]) == 6
assert total_pos_count([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 0
assert total_pos_count([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 9

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)