def sum_nested_list(nested_list):
    """
    Recursively calculates the sum of all integers in a nested list structure.

    Args:
        nested_list (list): A list which may contain integers and/or other nested lists.

    Returns:
        int: The sum of all integers within the nested list structure.
    """
    total_sum = 0

    for element in nested_list:
        if isinstance(element, list):
            # Recursively call the function if the element is a list
            total_sum += sum_nested_list(element)
        elif isinstance(element, int):
            # Add to total_sum if the element is an integer
            total_sum += element

    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_nested_list([1, [2, [3, 4], 5], 6]) == 21
assert sum_nested_list([[1, 2], [3, [4, 5]], 6]) == 21
assert sum_nested_list([1, 2, 3, 4, 5]) == 15
assert sum_nested_list([[[1], 2], [3, [4]], 5]) == 15
assert sum_nested_list([]) == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)