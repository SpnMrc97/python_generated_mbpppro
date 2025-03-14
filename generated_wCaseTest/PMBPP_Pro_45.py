def get_max_sum_list(lst):
    # Dictionary for memoization
    memo = {}

    def f(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        # Calculate the maximum value using the recursive function
        max_value = max(f(n // 2) + f(n // 3) + f(n // 4) + f(n // 5), n)
        memo[n] = max_value
        return max_value

    # Calculate the sum of maximum sums for each element in the list
    total_max_sum = sum(f(x) for x in lst)
    return total_max_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert get_max_sum_list([1, 2, 3]) == 6

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)