from functools import reduce
from operator import mul

def sum_of_multiplied_nums(list_of_lists):
    total_sum = 0
    for sublist in list_of_lists:
        if not sublist:
            continue  # Skip empty sublists to avoid division by zero
        # Calculate the product of all numbers in the sublist
        product = reduce(mul, sublist, 1)
        # Divide the product by the length of the sublist
        result = product / len(sublist)
        # Add the result to the total sum
        total_sum += result
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_multiplied_nums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 210.0
assert sum_of_multiplied_nums([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 12.0
assert sum_of_multiplied_nums([[10, 20], [30, 40], [50, 60]]) == 2200.0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)