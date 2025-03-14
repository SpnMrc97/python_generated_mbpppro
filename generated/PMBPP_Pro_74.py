def total_count(lists_of_bools):
    """
    Count the number of True values in multiple lists and return the total count across all lists.

    :param lists_of_bools: A list of lists containing boolean values.
    :return: The total count of True values across all lists.
    """
    total_true_count = 0
    for sublist in lists_of_bools:
        total_true_count += sum(1 for value in sublist if value is True)
    return total_true_count
