def total_pos_count(lists):
    """
    Count the number of positive numbers in multiple lists and return the total count.

    Args:
    lists (list of list of int/float): A list containing sublists of numbers.

    Returns:
    int: The total count of positive numbers across all sublists.
    """
    total_count = 0

    for sublist in lists:
        for number in sublist:
            if number > 0:
                total_count += 1

    return total_count
