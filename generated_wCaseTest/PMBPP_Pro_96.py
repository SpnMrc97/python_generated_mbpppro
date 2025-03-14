def total_sum_of_ranges(list_of_lists, m, n):
    """
    Calculate the total sum of all numbers in each sublist within the specified range of indices.

    Args:
        list_of_lists (List[List[int]]): A list containing sublists of integers.
        m (int): The starting index of the range (inclusive).
        n (int): The ending index of the range (inclusive).

    Returns:
        int: The total sum of the numbers in the specified range across all sublists.
    """
    total_sum = 0
    for sublist in list_of_lists:
        # Ensure the indices are within valid range for each sublist
        start_index = max(0, m)
        end_index = min(len(sublist), n + 1)

        # Sum the elements in the specified range and add to the total sum
        total_sum += sum(sublist[start_index:end_index])

    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_sum_of_ranges([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2) == 33
assert total_sum_of_ranges([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 0, 1) == 270
assert total_sum_of_ranges([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 0, 0) == 6

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)