def find_substring_in_lists(list_of_lists, sub_str):
    """
    Finds the indices of lists within list_of_lists where the substring sub_str is present.

    Args:
        list_of_lists (list of list of str): The list containing lists of strings.
        sub_str (str): The substring to search for.

    Returns:
        list of int: A list of indices where the substring is found, or an empty list if not found.
    """
    indices = []
    for index, string_list in enumerate(list_of_lists):
        for string in string_list:
            if sub_str in string:
                indices.append(index)
                break  # No need to check further strings in the current list
    return indices
