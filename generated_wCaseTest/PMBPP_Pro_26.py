from math import comb

def sum_even_binomial_coeffs(numbers):
    results = []
    for n in numbers:
        sum_even_indices = 0
        # Iterate over even indices
        for k in range(0, n + 1, 2):
            sum_even_indices += comb(n, k)
        results.append(sum_even_indices)
    return results

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_even_binomial_coeffs([1, 2, 3]) == [1, 2, 4]
assert sum_even_binomial_coeffs([4, 5, 6]) == [8, 16, 32]
assert sum_even_binomial_coeffs([7, 8, 9]) == [64, 128, 256]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)