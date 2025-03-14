def validate_list(numbers):
    def is_valid(number):
        digit_count = {}
        for digit in str(number):
            if digit not in digit_count:
                digit_count[digit] = 0
            digit_count[digit] += 1
        
        for digit, count in digit_count.items():
            if count > int(digit):
                return False
        return True

    return [is_valid(number) for number in numbers]

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert validate_list([123, 444, 55555]) == [True, True, True]
assert validate_list([1234, 555, 666666]) == [True, True, True]
assert validate_list([111, 222, 3333]) == [False, False, False]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)