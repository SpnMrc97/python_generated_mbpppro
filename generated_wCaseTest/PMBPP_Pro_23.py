def sum_of_sums_even_and_even_index(arr_of_arrs):
    total_sum = 0
    for sublist in arr_of_arrs:
        sublist_sum = 0
        for index, value in enumerate(sublist):
            if index % 2 == 0 and value % 2 == 0:
                sublist_sum += value
        total_sum += sublist_sum
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_sums_even_and_even_index([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 0
assert sum_of_sums_even_and_even_index([[1, 3, 5, 7], [2, 4, 6, 8], [10, 12, 14, 16]]) == 32
assert sum_of_sums_even_and_even_index([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]) == 4

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)