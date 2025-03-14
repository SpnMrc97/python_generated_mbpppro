from itertools import combinations_with_replacement
from typing import List, Dict, Tuple

def combinations_colors_by_lengths(colors: List[str], lengths: List[int]) -> Dict[int, List[Tuple[str, ...]]]:
    result = {}
    
    for length in lengths:
        # Generate combinations with replacement for the given length
        combos = list(combinations_with_replacement(colors, length))
        result[length] = combos
    
    return result

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert combinations_colors_by_lengths(['red', 'blue'], [1, 2]) == {1: [('red',), ('blue',)], 2: [('red', 'red'), ('red', 'blue'), ('blue', 'blue')]}
assert combinations_colors_by_lengths(['green', 'yellow', 'purple'], [2, 3]) == {2: [('green', 'green'), ('green', 'yellow'), ('green', 'purple'), ('yellow', 'yellow'), ('yellow', 'purple'), ('purple', 'purple')], 3: [('green', 'green', 'green'), ('green', 'green', 'yellow'), ('green', 'green', 'purple'), ('green', 'yellow', 'yellow'), ('green', 'yellow', 'purple'), ('green', 'purple', 'purple'), ('yellow', 'yellow', 'yellow'), ('yellow', 'yellow', 'purple'), ('yellow', 'purple', 'purple'), ('purple', 'purple', 'purple')]}

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)