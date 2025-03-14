def total_count_X(tuples_list, x):
    """
    Counts the total occurrences of a specified element across all tuples in the list.

    Parameters:
    tuples_list (list of tuple): The list of tuples to search through.
    x (any): The element to count occurrences of.

    Returns:
    int: The total count of occurrences of x in all tuples.
    """
    count = 0
    for tup in tuples_list:
        count += tup.count(x)
    return count
