def deep_extract_singly(nested_list):
    """
    Flattens a deeply nested list into a single set of numbers.

    :param nested_list: List containing numbers and/or other lists
    :return: A set of numbers extracted from the nested list
    """
    def flatten_helper(current_list):
        for item in current_list:
            if isinstance(item, list):
                yield from flatten_helper(item)
            else:
                yield item

    return set(flatten_helper(nested_list))

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert deep_extract_singly([1, 2, [3, 4], [[5], [6, 7]], [[[8]], 9]]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}
assert deep_extract_singly([[1, 2, [3]], [4, [5, 6]], [[7, [8]], 9]]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}
assert deep_extract_singly([[[[1]]], [[[[2]]]], [[[[[3]]]]]]) == {1, 2, 3}
assert deep_extract_singly([10, [20, [30, [40, [50]]]]]) == {10, 20, 30, 40, 50}
assert deep_extract_singly([]) == set()
assert deep_extract_singly([[1, 2], [2, 3], [3, 4, [4, 5]]]) == {1, 2, 3, 4, 5}

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)