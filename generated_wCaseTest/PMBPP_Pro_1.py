import re

def filter_lowercase_underscore_strings(strings):
    """
    Filters a list of strings, returning only those which contain
    sequences of lowercase letters joined with underscores.

    :param strings: List of strings to be filtered
    :return: A list of strings that match the pattern
    """
    pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    return [s for s in strings if pattern.match(s)]

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert filter_lowercase_underscore_strings(['abc_def', 'ghi_jkl', 'mno_pqr_stu', 'vwx_yz', 'ABC_DEF']) == ['abc_def', 'ghi_jkl', 'mno_pqr_stu', 'vwx_yz']
assert filter_lowercase_underscore_strings(['123_456', 'abc_def_123', 'ghi_jkl_', '_mno_pqr']) == []
assert filter_lowercase_underscore_strings([]) == []
assert filter_lowercase_underscore_strings(['abc_def', 'ghi_jkl', 'mno_pqr_stu', 'vwx_yz', 'abc_def_ghi']) == ['abc_def', 'ghi_jkl', 'mno_pqr_stu', 'vwx_yz', 'abc_def_ghi']

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)