def common_elements_count(nested_lists):
    if not nested_lists or not all(nested_lists):
        return {}

    # Find common elements across all nested lists
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)

    # Count occurrences of common elements in each nested list
    common_count_dict = {}
    for element in common_elements:
        counts = [lst.count(element) for lst in nested_lists]
        common_count_dict[element] = counts

    return common_count_dict

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert common_elements_count([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) == {3: [1, 1, 1]};
assert common_elements_count([[1, 1, 1], [1, 2, 2], [1, 3, 3]]) == {1: [3, 1, 1]};
assert common_elements_count([[10, 20], [20, 30], [30, 40]]) == {}
assert common_elements_count([['a', 'b'], ['b', 'c'], ['c', 'd']]) == {}

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)