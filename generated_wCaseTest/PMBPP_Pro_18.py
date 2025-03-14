def split_list_by_lengths(lst, lengths):
    """
    Splits a list into parts based on specified lengths.

    Parameters:
    lst (list): The list to be split.
    lengths (list of int): A list of integers specifying the lengths of each part.

    Returns:
    list of lists: A list containing the split parts, or an empty list if the lengths do not sum up to the length of the list.
    """
    if sum(lengths) != len(lst):
        return []

    result = []
    index = 0

    for length in lengths:
        if index + length > len(lst):
            return []
        result.append(lst[index:index + length])
        index += length

    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert split_list_by_lengths([1, 2, 3, 4, 5], [2, 3]) == [[1, 2], [3, 4, 5]]
assert split_list_by_lengths([1, 2, 3, 4, 5], [1, 2, 2]) == [[1], [2, 3], [4, 5]]
assert split_list_by_lengths([1, 2, 3, 4, 5], [1, 4]) == [[1], [2, 3, 4, 5]]
assert split_list_by_lengths([], [0]) == [[]]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)