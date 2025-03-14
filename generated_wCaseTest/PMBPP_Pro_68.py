from collections import defaultdict

def flatten(nested_list):
    """Flatten a nested list of arbitrary depth."""
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element

def frequency_nested_lists(nested_list):
    """Calculate the frequency of each element in a nested list."""
    frequency_dict = defaultdict(int)
    
    for element in flatten(nested_list):
        frequency_dict[element] += 1
        
    return dict(frequency_dict)

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert frequency_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) == {1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
assert frequency_nested_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
assert frequency_nested_lists([[[[1], [2, 3]], [[4], [5, 6]]], [[[7], [8, 9]], [[10], [11, 12]]]]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)