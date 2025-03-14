def sum_of_squares_list(numbers):
    def sum_of_squares_of_first_n_even_numbers(n):
        # Calculate the sum of squares of the first n even natural numbers
        return sum((2 * i) ** 2 for i in range(1, n + 1))
    
    return [sum_of_squares_of_first_n_even_numbers(n) for n in numbers]

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_squares_list([1, 2, 3]) == [4.0, 20.0, 56.0]
assert sum_of_squares_list([0, 4, 5]) == [0.0, 120.0, 220.0]
assert sum_of_squares_list([10]) == [1540.0]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)