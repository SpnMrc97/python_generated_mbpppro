def is_sequence_of_sublists(list_of_lists, sequence_of_sublists):
    if not sequence_of_sublists:  # An empty sequence is trivially found
        return True
    
    len_main = len(list_of_lists)
    len_seq = len(sequence_of_sublists)

    # Iterate through the main list to find the start of the sequence
    for i in range(len_main - len_seq + 1):
        # Check if the sublist from i to i + len_seq matches the sequence
        if list_of_lists[i:i + len_seq] == sequence_of_sublists:
            return True

    return False

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert is_sequence_of_sublists([[1, 2], [3, 4], [5, 6], [7, 8]], [[3, 4], [5, 6]]) == True
assert is_sequence_of_sublists([[1, 2], [3, 4], [5, 6], [7, 8]], [[3, 4], [7, 8]]) == False
assert is_sequence_of_sublists([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2], [3, 4], [5, 6], [7, 8]]) == True
assert is_sequence_of_sublists([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2], [3, 4], [7, 8]]) == False

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)