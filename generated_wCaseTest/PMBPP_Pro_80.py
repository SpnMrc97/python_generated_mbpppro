def max_product_nested_list(nested_list):
    """
    Given a list of lists of tuples, where each tuple contains two numbers,
    finds the maximum absolute product between numbers in pairs of tuples
    across all sublists.

    Args:
        nested_list (list): A list of lists, where each sublist contains tuples
                            of two numbers.

    Returns:
        int or float: The maximum absolute product found.
    """
    max_product = float('-inf')  # Initialize to negative infinity to ensure any product is larger

    # Iterate over each sublist
    for sublist in nested_list:
        # Iterate over each tuple in the sublist
        for num1, num2 in sublist:
            # Calculate the absolute product of the tuple
            product = abs(num1 * num2)
            # Update max_product if the current product is greater
            if product > max_product:
                max_product = product

    return max_product

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert max_product_nested_list([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]) == 56
assert max_product_nested_list([[(1, -1), (2, -2)], [(3, -3), (4, -4)]]) == 16
assert max_product_nested_list([[(0, 0), (0, 0)], [(0, 0), (0, 0)]]) == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)