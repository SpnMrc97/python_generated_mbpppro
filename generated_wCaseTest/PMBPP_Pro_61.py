def sum_centered_hexagonal_numbers(points):
    def centered_hexagonal_number(n):
        return 3 * n * (n - 1) + 1

    total_sum = 0
    for point in points:
        total_sum += centered_hexagonal_number(point)
    
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_centered_hexagonal_numbers([1, 2, 3]) == 27
assert sum_centered_hexagonal_numbers([4, 5]) == 98
assert sum_centered_hexagonal_numbers([10]) == 271

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)