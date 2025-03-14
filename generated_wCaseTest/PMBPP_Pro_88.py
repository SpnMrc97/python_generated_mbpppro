def sum_of_hexagonal_numbers(N):
    """
    Calculate the sum of the first N hexagonal numbers.

    Parameters:
    N (int): The number of hexagonal numbers to sum.

    Returns:
    int: The sum of the first N hexagonal numbers.
    """
    if N < 1:
        raise ValueError("N must be a positive integer")

    hexagonal_sum = sum(n * (2 * n - 1) for n in range(1, N + 1))
    return hexagonal_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_hexagonal_numbers(1) == 1
assert sum_of_hexagonal_numbers(2) == 7
assert sum_of_hexagonal_numbers(3) == 22
assert sum_of_hexagonal_numbers(4) == 50

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)