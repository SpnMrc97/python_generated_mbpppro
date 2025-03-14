def complex_sort(list_of_lists):
    """
    Sorts each sublist in the given list of lists in ascending order, then sorts
    the main list based on the sum of elements in each sublist.

    Parameters:
    list_of_lists (list of list of int): A list containing sublists of integers.

    Returns:
    list of list of int: The sorted list of lists.
    """
    # First, sort each sublist individually
    sorted_sublists = [sorted(sublist) for sublist in list_of_lists]
    
    # Then, sort the list of sorted sublists based on the sum of each sublist
    sorted_main_list = sorted(sorted_sublists, key=sum)
    
    return sorted_main_list
