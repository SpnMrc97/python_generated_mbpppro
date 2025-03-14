def total_frequency(list_of_lists, x):
    """
    Counts the total number of occurrences of a specific number across all sublists.

    Parameters:
    list_of_lists (list of list of int): A list containing sublists of integers.
    x (int): The number to count occurrences of.

    Returns:
    int: The total number of occurrences of x across all sublists.
    """
    count = 0
    for sublist in list_of_lists:
        count += sublist.count(x)
    return count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_frequency([[1, 2, 2], [2, 3, 4], [2, 2, 2]], 2) == 6
assert total_frequency([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1) == 9
assert total_frequency([[5, 5], [5, 5, 5], [5]], 5) == 6
assert total_frequency([[10, 20], [30, 40], [50]], 100) == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)