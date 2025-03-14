def check_elements_in_lists(list_of_lists, element):
    """
    This function takes a list of lists and an element. It returns a list of booleans
    indicating whether all items in each sublist are equal to the given element.

    :param list_of_lists: List[List[Any]] - A list of sublists to be checked.
    :param element: Any - The element to compare against each item in the sublists.
    :return: List[bool] - A list of booleans where each boolean corresponds to whether
                          all items in a sublist are equal to the element.
    """
    return [all(item == element for item in sublist) for sublist in list_of_lists]

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert check_elements_in_lists([[1, 1, 1], [2, 2, 2], [1, 1, 1]], 1) == [True, False, True]
assert check_elements_in_lists([[3, 3], [3, 3], [3, 3]], 3) == [True, True, True]
assert check_elements_in_lists([[4, 5], [5, 5], [5, 4]], 5) == [False, True, False]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)