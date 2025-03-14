def len_longest_word_in_sentences(sentences):
    """
    This function takes a list of sentences and returns the length of the longest word across all sentences.
    
    :param sentences: List of sentences (strings)
    :return: Integer representing the length of the longest word
    """
    max_length = 0
    
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into words
        for word in words:
            # Update max_length if the current word's length is greater
            max_length = max(max_length, len(word))
    
    return max_length

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert len_longest_word_in_sentences(['The quick brown fox', 'jumps over the lazy dog']) == 5
assert len_longest_word_in_sentences(['Python is fun', 'Programming is awesome']) == 11
assert len_longest_word_in_sentences(['Hello world', 'Goodbye']) == 7
assert len_longest_word_in_sentences(['Short', 'Longestwordhere']) == 15

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)