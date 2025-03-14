def find_numbers_in_range(start, end):
    def reverse_number(n):
        return int(str(n)[::-1])

    result = []
    for number in range(start, end + 1):
        reversed_number = reverse_number(number)
        if number == 2 * reversed_number - 1:
            result.append(number)
    
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert find_numbers_in_range(10, 100) == [73]
assert find_numbers_in_range(100, 200) == []
assert find_numbers_in_range(1000, 1100) == []

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)