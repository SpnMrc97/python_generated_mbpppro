def check_types_in_list(tuple_list):
    """
    Check if each tuple in the list has elements of the same data type.

    Parameters:
    tuple_list (list): A list of tuples to be checked.

    Returns:
    list: A list of boolean values where each value corresponds to whether
          the elements in the respective tuple have the same data type.
    """
    result = []
    
    for tup in tuple_list:
        # Extract the data types of each element in the tuple
        types = set(type(element) for element in tup)
        
        # Check if all elements in the tuple have the same data type
        result.append(len(types) == 1)
    
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert check_types_in_list([(1, 2, 3), ('a', 'b', 'c'), (1, 'a', 3)]) == [True, True, False]
assert check_types_in_list([(True, False), (1.0, 2.0, 3.0), ('hello', 123)]) == [True, True, False]
assert check_types_in_list([(1, 1, 1), ('a', 'a', 'a'), (True, True, True)]) == [True, True, True]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)