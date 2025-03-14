def sum_of_tetrahedral_numbers(k):
    def tetrahedral_number(n):
        """Calculate the n-th tetrahedral number."""
        return n * (n + 1) * (n + 2) // 6
    
    total_sum = 0
    for i in range(1, k + 1):
        total_sum += tetrahedral_number(i)
    
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_tetrahedral_numbers(1) == 1
assert sum_of_tetrahedral_numbers(2) == 5.0
assert sum_of_tetrahedral_numbers(3) == 15.0
assert sum_of_tetrahedral_numbers(4) == 35.0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)