def chained_subtract_elements(tuple_list):
    if not tuple_list:
        raise ValueError("The list of tuples must not be empty.")
    
    # Start with the first tuple in the list as the initial result
    result = tuple_list[0]
    
    # Iterate over the tuples starting from the second one
    for next_tuple in tuple_list[1:]:
        # Subtract each element of the result tuple by the corresponding element in the next_tuple
        result = tuple(a - b for a, b in zip(result, next_tuple))
    
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert chained_subtract_elements([(10, 20, 30), (5, 5, 5), (2, 2, 2)]) == (3, 13, 23)
assert chained_subtract_elements([(100, 200), (10, 20), (5, 10)]) == (85, 170)
assert chained_subtract_elements([(1, 1, 1), (1, 1, 1), (1, 1, 1)]) == (-1, -1, -1)

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)