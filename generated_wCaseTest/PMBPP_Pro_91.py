def complex_sort(list_of_lists):
    """
    Sorts each sublist in the given list of lists in ascending order, then sorts
    the main list based on the sum of elements in each sublist.

    Parameters:
    list_of_lists (list of list of int): A list containing sublists of integers.

    Returns:
    list of list of int: The sorted list of lists.
    """
    # First, sort each sublist individually
    sorted_sublists = [sorted(sublist) for sublist in list_of_lists]
    
    # Then, sort the list of sorted sublists based on the sum of each sublist
    sorted_main_list = sorted(sorted_sublists, key=sum)
    
    return sorted_main_list

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert complex_sort([[3, 1, 2], [5, 4], [6]]) == [[1, 2, 3], [6], [4, 5]]
assert complex_sort([[9, 8, 7], [6, 5], [4, 3, 2, 1]]) == [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
assert complex_sort([[10], [20, 30], [40, 50, 60]]) == [[10], [20, 30], [40, 50, 60]]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)