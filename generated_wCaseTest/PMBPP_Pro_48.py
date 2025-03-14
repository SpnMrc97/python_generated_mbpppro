def total_sum_of_digits(lists_of_nums):
    total_sum = 0
    for sublist in lists_of_nums:
        for number in sublist:
            # Convert the number to a string to iterate over each digit
            digits = str(abs(number))
            # Sum the digits of the number
            sum_of_digits = sum(int(digit) for digit in digits)
            # Add to the total sum
            total_sum += sum_of_digits
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert total_sum_of_digits([[123, 456], [789, 12]]) == 48
assert total_sum_of_digits([[0, 1], [2, 3]]) == 6
assert total_sum_of_digits([[10, 20], [30, 40]]) == 10
assert total_sum_of_digits([[111, 222], [333, 444]]) == 30
assert total_sum_of_digits([[555, 666], [777, 888]]) == 78

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)