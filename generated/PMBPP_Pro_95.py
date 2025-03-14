def total_frequency(list_of_lists, x):
    """
    Counts the total number of occurrences of a specific number across all sublists.

    Parameters:
    list_of_lists (list of list of int): A list containing sublists of integers.
    x (int): The number to count occurrences of.

    Returns:
    int: The total number of occurrences of x across all sublists.
    """
    count = 0
    for sublist in list_of_lists:
        count += sublist.count(x)
    return count
