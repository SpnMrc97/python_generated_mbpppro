def sum_of_quotients(operations):
    """
    Calculate the sum of quotients rounded down to the nearest integer
    for each tuple in the list.

    :param operations: List of tuples, where each tuple contains two integers
                       (numerator, denominator).
    :return: Sum of all integer quotients.
    """
    total_sum = 0
    for numerator, denominator in operations:
        if denominator == 0:
            raise ValueError("Division by zero error in operations list.")
        quotient = numerator // denominator
        total_sum += quotient
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_of_quotients([(10, 3), (7, 2), (15, 4)]) == 9
assert sum_of_quotients([(20, 5), (9, 3), (12, 4)]) == 10
assert sum_of_quotients([(100, 10), (81, 9), (64, 8)]) == 27

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)