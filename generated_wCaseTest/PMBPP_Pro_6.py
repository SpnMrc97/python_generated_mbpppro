def total_number_of_substrings(str_list):
    """
    Calculate the total number of non-empty substrings for each string in the list and return the sum.

    Args:
    str_list (list of str): A list of strings.

    Returns:
    int: The sum of non-empty substrings of each string in the list.
    """
    total_count = 0
    for s in str_list:
        n = len(s)
        total_count += (n * (n + 1)) // 2
    return total_count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_number_of_substrings(['abc', 'def']) == 12
assert total_number_of_substrings(['', 'a']) == 1
assert total_number_of_substrings(['hello', 'world']) == 30
assert total_number_of_substrings(['python', 'programming']) == 87

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)