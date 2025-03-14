def sum_negativenums(nums_list):
    """
    Calculate the sum of all negative numbers in each sublist and return a list of these sums.

    :param nums_list: List of lists containing numbers.
    :return: List containing the sum of negative numbers for each sublist.
    """
    negative_sums = []
    for sublist in nums_list:
        # Calculate the sum of negative numbers in the current sublist
        negative_sum = sum(num for num in sublist if num < 0)
        # Append the result to the negative_sums list
        negative_sums.append(negative_sum)
    
    return negative_sums

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_negativenums([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]) == [-2, -10, -8]
assert sum_negativenums([[0, -1], [2, 3], [-4, -5]]) == [-1, 0, -9]
assert sum_negativenums([[], [1, -1], [-2, 2]]) == [0, -1, -2]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)