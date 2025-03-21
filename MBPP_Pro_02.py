import heapq
from typing import List

def find_n_largest_from_lists(lists: List[List[int]], n: int) -> List[int]:
    result = []
    
    for sublist in lists:
        # Find the n largest elements in the sublist
        largest_in_sublist = heapq.nlargest(n, sublist)
        # Add them to the result list
        result.extend(largest_in_sublist)
    
    # Sort the result list in descending order
    result.sort(reverse=True)
    
    return result
