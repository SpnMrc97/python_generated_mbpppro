def sum_of_square_sums(lst):
    def sum_of_squares_of_first_n_odds(n):
        # Calculate the sum of squares of the first n odd numbers
        sum_of_squares = 0
        for i in range(n):
            odd_number = 2 * i + 1  # Generate the ith odd number
            sum_of_squares += odd_number ** 2
        return sum_of_squares
    
    total_sum = 0
    for n in lst:
        total_sum += sum_of_squares_of_first_n_odds(n)
    
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_square_sums([1, 2, 3]) == 46

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)