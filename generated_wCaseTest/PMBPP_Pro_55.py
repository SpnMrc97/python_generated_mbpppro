def sort_list_of_lists(list_of_lists):
    # Sort each sublist
    sorted_sublists = [sorted(sublist) for sublist in list_of_lists]
    
    # Sort the main list based on the sum of elements in each sublist
    sorted_main_list = sorted(sorted_sublists, key=sum)
    
    return sorted_main_list

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sort_list_of_lists([[3, 2, 1], [6, 5, 4], [9, 8, 7]]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert sort_list_of_lists([[10, 20], [1], [3, 4, 5]]) == [[1], [3, 4, 5], [10, 20]]
assert sort_list_of_lists([[15, 15], [10, 10, 10], [5, 5, 5, 5]]) == [[5, 5, 5, 5], [15, 15], [10, 10, 10]]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)