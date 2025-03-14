def convert_and_concatenate_binary(decimal_list):
    # Convert each decimal number to binary and strip the '0b' prefix
    binary_strings = [bin(number)[2:] for number in decimal_list]
    
    # Concatenate all binary strings
    concatenated_binary = ''.join(binary_strings)
    
    # Remove leading zeros from the final result
    result = concatenated_binary.lstrip('0')
    
    # Return the result, or '0' if the result is an empty string
    return result if result else '0'

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert convert_and_concatenate_binary([10, 20, 30]) == '10101010011110'
assert convert_and_concatenate_binary([0, 1, 2]) == '110'
assert convert_and_concatenate_binary([128, 64, 32]) == '100000001000000100000'

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)