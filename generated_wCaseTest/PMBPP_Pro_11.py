def total_count_X(tuples_list, x):
    """
    Counts the total occurrences of a specified element across all tuples in the list.

    Parameters:
    tuples_list (list of tuple): The list of tuples to search through.
    x (any): The element to count occurrences of.

    Returns:
    int: The total count of occurrences of x in all tuples.
    """
    count = 0
    for tup in tuples_list:
        count += tup.count(x)
    return count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_count_X([(1, 2, 3), (2, 3, 4), (3, 4, 5)], 3) == 3
assert total_count_X([('a', 'b', 'a'), ('b', 'c', 'c'), ('a', 'c', 'a')], 'a') == 4
assert total_count_X([(1, 'a', 1), ('b', 1, 'b'), (1, 'c', 1)], 1) == 5
assert total_count_X([(True, False, True), (False, True, False), (True, True, True)], True) == 6
assert total_count_X([(1, 2, 3), ('a', 'b', 'c'), (True, False, True)], 'd') == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)