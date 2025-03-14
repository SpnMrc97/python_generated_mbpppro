def first_non_repeating_characters(strings):
    result = []
    for string in strings:
        # Dictionary to count the occurrences of each character
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the first non-repeated character
        non_repeated_char = None
        for char in string:
            if char_count[char] == 1:
                non_repeated_char = char
                break
        
        result.append(non_repeated_char)
    
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert first_non_repeating_characters(['abacddbec', 'abc', 'aabbcc']) == ['e', 'a', None]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)