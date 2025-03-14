from itertools import combinations_with_replacement
from typing import List, Dict, Tuple

def combinations_colors_by_lengths(colors: List[str], lengths: List[int]) -> Dict[int, List[Tuple[str, ...]]]:
    result = {}
    
    for length in lengths:
        # Generate combinations with replacement for the given length
        combos = list(combinations_with_replacement(colors, length))
        result[length] = combos
    
    return result
