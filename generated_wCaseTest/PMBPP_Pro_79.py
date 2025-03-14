def find_all_unique_elements(arrays):
    from collections import defaultdict
    
    # Dictionary to hold the count of each element
    element_count = defaultdict(int)
    
    # Iterate over each array
    for array in arrays:
        # Iterate over each element in the array
        for element in array:
            # Increment the count of the element
            element_count[element] += 1
    
    # Find and return elements that appear once
    unique_elements = [element for element, count in element_count.items() if count == 1]
    
    return unique_elements

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert find_all_unique_elements([[1, 1, 2, 3, 3], [4, 4, 5, 6, 6], [7, 7, 8, 8, 9]]) == [2, 5, 9]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)