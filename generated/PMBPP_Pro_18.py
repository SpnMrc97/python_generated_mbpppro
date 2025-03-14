def split_list_by_lengths(lst, lengths):
    """
    Splits a list into parts based on specified lengths.

    Parameters:
    lst (list): The list to be split.
    lengths (list of int): A list of integers specifying the lengths of each part.

    Returns:
    list of lists: A list containing the split parts, or an empty list if the lengths do not sum up to the length of the list.
    """
    if sum(lengths) != len(lst):
        return []

    result = []
    index = 0

    for length in lengths:
        if index + length > len(lst):
            return []
        result.append(lst[index:index + length])
        index += length

    return result
