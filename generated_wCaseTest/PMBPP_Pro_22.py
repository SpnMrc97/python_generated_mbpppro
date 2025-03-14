def sum_ascii_values(s):
    """
    Calculate the sum of the ASCII values of all characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII values of the characters in the string.
    """
    return sum(ord(char) for char in s)

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_ascii_values('') == 0
assert sum_ascii_values('A') == 65
assert sum_ascii_values('hello') == 532
assert sum_ascii_values('Python') == 642
assert sum_ascii_values('123') == 150

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)