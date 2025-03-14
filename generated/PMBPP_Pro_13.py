def total_integer_count(list_of_lists):
    """
    Calculate the total number of integer elements across all sublists.

    :param list_of_lists: A list containing multiple lists.
    :return: The total count of integer elements in all sublists.
    """
    total_count = 0
    for sublist in list_of_lists:
        for element in sublist:
            if isinstance(element, int):
                total_count += 1
    return total_count
