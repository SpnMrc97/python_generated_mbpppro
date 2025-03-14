def is_palindrome(n):
    """Check if an integer is a palindrome."""
    s = str(n)
    return s == s[::-1]

def next_smallest_palindrome(n):
    """Find the next smallest palindrome greater than the given number."""
    while True:
        n += 1
        if is_palindrome(n):
            return n

def sum_of_next_smallest_palindromes(nums):
    """Calculate the sum of the next smallest palindromes for each number in the list."""
    if not nums:
        return 0

    total = 0
    for num in nums:
        palindrome = next_smallest_palindrome(num)
        total += palindrome
    
    return total

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_next_smallest_palindromes([123, 121, 999]) == 131 + 131 + 1001
assert sum_of_next_smallest_palindromes([191, 202, 303]) == 202 + 212 + 313
assert sum_of_next_smallest_palindromes([]) == 0
assert sum_of_next_smallest_palindromes([888, 999, 1001]) == 898 + 1001 + 1111

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)