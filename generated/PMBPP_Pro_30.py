def all_sublists_unique(list_of_lists):
    """
    Check if all sublists within the list of lists have unique elements.

    :param list_of_lists: A list of lists to be checked.
    :return: True if all sublists have unique elements, False otherwise.
    """
    for sublist in list_of_lists:
        if len(sublist) != len(set(sublist)):
            return False
    return True
