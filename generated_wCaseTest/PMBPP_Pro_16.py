def swap_all_numbers(tuples_list):
    """
    Swaps the two numbers in each tuple within a list of tuples.

    Parameters:
    tuples_list (list of tuples): A list where each element is a tuple containing two numbers.

    Returns:
    list of tuples: A new list of tuples with the numbers in each tuple swapped.
    """
    # List comprehension to swap numbers in each tuple
    swapped_tuples = [(b, a) for a, b in tuples_list]
    return swapped_tuples

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert swap_all_numbers([(1, 2), (3, 4), (5, 6)]) == [(2, 1), (4, 3), (6, 5)]
assert swap_all_numbers([(10, 20), (30, 40)]) == [(20, 10), (40, 30)]
assert swap_all_numbers([]) == []
assert swap_all_numbers([(7, 8)]) == [(8, 7)]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)