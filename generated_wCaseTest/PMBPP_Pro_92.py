def count_same_items_in_lists(list_of_lists):
    if not list_of_lists or not all(list_of_lists):
        return 0

    # Transpose the list of lists to group elements by their positions
    transposed_lists = zip(*list_of_lists)

    identical_count = 0

    # Iterate through each group of elements by position
    for group in transposed_lists:
        # Check if all elements in the group are the same
        if all(element == group[0] for element in group):
            identical_count += 1

    return identical_count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert count_same_items_in_lists([[1, 2, 3], [1, 2, 4], [1, 2, 5]]) == 2
assert count_same_items_in_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == 3
assert count_same_items_in_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
assert count_same_items_in_lists([[1, 'a', 3.14], [1, 'b', 3.14], [1, 'c', 3.14]]) == 2
assert count_same_items_in_lists([[], [], []]) == 0

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)