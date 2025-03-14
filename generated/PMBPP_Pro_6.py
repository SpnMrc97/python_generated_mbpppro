def total_number_of_substrings(str_list):
    """
    Calculate the total number of non-empty substrings for each string in the list and return the sum.

    Args:
    str_list (list of str): A list of strings.

    Returns:
    int: The sum of non-empty substrings of each string in the list.
    """
    total_count = 0
    for s in str_list:
        n = len(s)
        total_count += (n * (n + 1)) // 2
    return total_count
