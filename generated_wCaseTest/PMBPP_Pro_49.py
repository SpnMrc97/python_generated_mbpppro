from heapq import nlargest
from typing import List

def find_n_largest_from_lists(lists: List[List[int]], n: int) -> List[int]:
    # Initialize a list to store the largest elements
    largest_elements = []

    # Iterate over each sublist in the list of lists
    for sublist in lists:
        # Find the n largest elements in the current sublist
        largest_in_sublist = nlargest(n, sublist)
        # Extend the largest_elements list with these elements
        largest_elements.extend(largest_in_sublist)

    # Sort the collected largest elements in descending order
    largest_elements.sort(reverse=True)

    return largest_elements

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert find_n_largest_from_lists([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]], 2) == [1001, 1000, 39, 37, 27, 26, 5, 4]
assert find_n_largest_from_lists([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]], 1) == [1001, 39, 27, 5]
assert find_n_largest_from_lists([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]], 3) == [1001, 1000, 857, 39, 37, 35, 27, 26, 18, 5, 4, 3]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)