from functools import reduce
import operator

def product_of_powers(tuples_list):
    """
    Calculate the product of all the resulting powers from a list of tuples.

    Args:
        tuples_list (list of tuples): Each tuple contains two integers (base, exponent).

    Returns:
        int: The product of all base raised to the exponent.
    """
    # Calculate the power for each tuple and store in a list
    powers = [base ** exponent for base, exponent in tuples_list]
    
    # Use reduce to compute the product of all elements in the powers list
    product = reduce(operator.mul, powers, 1)
    
    return product

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert product_of_powers([(2, 3), (4, 2), (5, 1)]) == 640
assert product_of_powers([(1, 1), (2, 2), (3, 3)]) == 108
assert product_of_powers([(0, 1), (10, 0), (1, 10)]) == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)