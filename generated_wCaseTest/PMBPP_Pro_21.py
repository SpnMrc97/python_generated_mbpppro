def sum_star_nums(k):
    """
    Calculate the sum of the first k star numbers.

    Parameters:
    k (int): The number of star numbers to sum.

    Returns:
    int: The sum of the first k star numbers.
    """
    if k < 1:
        return 0
    
    total_sum = 0
    for n in range(1, k + 1):
        star_number = 6 * n * (n - 1) + 1
        total_sum += star_number
    
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_star_nums(1) == 1
assert sum_star_nums(2) == 14
assert sum_star_nums(3) == 51
assert sum_star_nums(4) == 124

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)