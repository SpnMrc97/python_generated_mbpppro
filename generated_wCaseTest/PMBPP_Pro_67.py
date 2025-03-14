def total_divisors(lst):
    def count_divisors(n):
        """Returns the number of divisors of a given integer n."""
        if n <= 0:
            return 0
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count

    total_count = 0
    for number in lst:
        total_count += count_divisors(number)
    
    return total_count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_divisors([1, 2, 3, 4, 5]) == 10
assert total_divisors([10, 20, 30]) == 18
assert total_divisors([11, 13, 17]) == 6

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)