def decagonal_number(n):
    """Calculate the n-th decagonal number."""
    return 4 * n ** 2 - 3 * n

def sum_of_decagonal_numbers(lst):
    """Calculate the sum of the first 10 decagonal numbers for each integer in the list."""
    results = []
    for num in lst:
        if num < 0:
            results.append(0)
        else:
            # Calculate the sum of the first 10 decagonal numbers
            sum_decagonal = sum(decagonal_number(i) for i in range(1, 11))
            results.append(sum_decagonal)
    return results

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_decagonal_numbers([1, 2, 3]) == [1375, 1375, 1375]
assert sum_of_decagonal_numbers([-1, 0, 1]) == [0, 1375, 1375]
assert sum_of_decagonal_numbers([5, 10, 15]) == [1375, 1375, 1375]
assert sum_of_decagonal_numbers([-5, -10, -15]) == [0, 0, 0]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)