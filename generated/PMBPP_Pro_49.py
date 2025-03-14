from heapq import nlargest
from typing import List

def find_n_largest_from_lists(lists: List[List[int]], n: int) -> List[int]:
    # Initialize a list to store the largest elements
    largest_elements = []

    # Iterate over each sublist in the list of lists
    for sublist in lists:
        # Find the n largest elements in the current sublist
        largest_in_sublist = nlargest(n, sublist)
        # Extend the largest_elements list with these elements
        largest_elements.extend(largest_in_sublist)

    # Sort the collected largest elements in descending order
    largest_elements.sort(reverse=True)

    return largest_elements
