from heapq import nlargest
from itertools import product

def large_products_from_pairs(list_pairs, N):
    """
    Given multiple pairs of lists, find the specified number of largest products
    from each pair of lists, selecting one factor from each list in each pair.
    
    :param list_pairs: List of tuples, where each tuple contains two lists of numbers.
    :param N: The number of largest products to return for each pair.
    :return: A list of lists, where each inner list contains the N largest products
             for the corresponding pair of input lists.
    """
    
    largest_products_per_pair = []

    for list1, list2 in list_pairs:
        # Generate all possible products
        products = [a * b for a, b in product(list1, list2)]
        # Find the N largest products
        largest_products = nlargest(N, products)
        largest_products_per_pair.append(largest_products)

    return largest_products_per_pair
