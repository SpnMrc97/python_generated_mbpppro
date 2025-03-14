def three_odd_length_words(words):
    """
    Determine if a list of words contains exactly three words with odd lengths.

    Args:
    words (list of str): A list of words to check.

    Returns:
    bool: True if there are exactly three words with odd lengths, False otherwise.
    """
    odd_length_count = sum(1 for word in words if len(word) % 2 != 0)
    return odd_length_count == 3

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert three_odd_length_words(['apple', 'banana', 'cherry', 'date']) == False
assert three_odd_length_words(['apple', 'banana', 'cherry']) == False
assert three_odd_length_words(['odd', 'even', 'odd', 'even', 'odd']) == True
assert three_odd_length_words([]) == False

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)