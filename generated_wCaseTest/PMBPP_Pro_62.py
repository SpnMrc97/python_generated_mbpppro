def find_all_char_long(texts):
    result = []
    for text in texts:
        words = text.split()
        long_words = [word for word in words if len(word) >= 4]
        result.append(long_words)
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert find_all_char_long(['This is a test', 'Another test string', 'Short words']) == [['This', 'test'], ['Another', 'test', 'string'], ['Short', 'words']]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)