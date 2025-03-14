def total_count(lists_of_bools):
    """
    Count the number of True values in multiple lists and return the total count across all lists.

    :param lists_of_bools: A list of lists containing boolean values.
    :return: The total count of True values across all lists.
    """
    total_true_count = 0
    for sublist in lists_of_bools:
        total_true_count += sum(1 for value in sublist if value is True)
    return total_true_count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_count([[True, False, True], [False, True, True]]) == 4
assert total_count([[False, False], [True, True, True]]) == 3
assert total_count([[], [True, False, True]]) == 2
assert total_count([[False, False, False], [False, False]]) == 0
assert total_count([[True], [True], [True]]) == 3

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)