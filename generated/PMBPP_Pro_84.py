from functools import reduce
from operator import mul

def product_of_list(lst):
    """
    Calculate the product of all elements in the list.

    Parameters:
    lst (list): A list of integers.

    Returns:
    int: The product of all integers in the list. If the list is empty, returns 1.
    """
    if not lst:
        return 1  # Return 1 for an empty list as the product of no numbers is conventionally 1
    
    return reduce(mul, lst, 1)
