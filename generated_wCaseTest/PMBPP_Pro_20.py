def find_duplicate_arrays(arrays):
    """
    This function checks each array in a list of arrays for duplicate elements.
    It returns a list of indices of arrays that contain duplicates.

    :param arrays: List of arrays (lists of integers)
    :return: List of indices of arrays with duplicate elements
    """
    duplicate_indices = []

    for index, array in enumerate(arrays):
        if len(array) != len(set(array)):
            duplicate_indices.append(index)

    return duplicate_indices

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert find_duplicate_arrays([[1, 2, 3], [4, 5, 4], [6, 7, 8]]) == [1]
assert find_duplicate_arrays([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == []
assert find_duplicate_arrays([[1, 1, 2], [3, 4, 5], [6, 6, 7]]) == [0, 2]
assert find_duplicate_arrays([[1], [2], [3]]) == []
assert find_duplicate_arrays([[1, 2, 2], [3, 3, 4], [5, 6, 5]]) == [0, 1, 2]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)