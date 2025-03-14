def all_sublists_unique(list_of_lists):
    """
    Check if all sublists within the list of lists have unique elements.

    :param list_of_lists: A list of lists to be checked.
    :return: True if all sublists have unique elements, False otherwise.
    """
    for sublist in list_of_lists:
        if len(sublist) != len(set(sublist)):
            return False
    return True

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert all_sublists_unique([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == True
assert all_sublists_unique([[1, 2, 2], [4, 5, 6], [7, 8, 9]]) == False
assert all_sublists_unique([[1, 2, 3], [4, 5, 6], [7, 7, 9]]) == False
assert all_sublists_unique([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == True

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)