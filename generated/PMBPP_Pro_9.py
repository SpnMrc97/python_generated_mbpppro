def count_total_chars(str_list):
    """
    Count the total number of characters in all strings combined in the provided list.

    Parameters:
    str_list (list of str): A list containing strings whose characters are to be counted.

    Returns:
    int: Total number of characters in all strings combined.
    """
    if not isinstance(str_list, list) or not all(isinstance(s, str) for s in str_list):
        raise ValueError("Input must be a list of strings.")
    
    total_chars = sum(len(s) for s in str_list)
    return total_chars
