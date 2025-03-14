from collections import ChainMap

def merge_dictionaries_list(dict_list):
    """
    Merges a list of dictionaries into a single dictionary.

    :param dict_list: List of dictionaries to merge
    :return: A single dictionary containing all key-value pairs from the input dictionaries
    """
    # Using ChainMap to merge dictionaries
    merged_dict = dict(ChainMap(*dict_list))
    return merged_dict

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert merge_dictionaries_list([{'a': 1}, {'b': 2}, {'c': 3}]) == {'a': 1, 'b': 2, 'c': 3}
assert merge_dictionaries_list([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) == {'b': 2, 'c': 4, 'a': 1}
assert merge_dictionaries_list([{}, {'a': 1}, {'b': 2}]) == {'a': 1, 'b': 2}
assert merge_dictionaries_list([{'a': 1}, {'a': 2}, {'a': 3}]) == {'a': 1}

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)