def insert_element_in_nested_list(nested_list, element):
    """
    Inserts a specified element before each element in each sublist of the nested list.

    Parameters:
    nested_list (list of lists): The nested list to be modified.
    element: The element to insert before each element in the sublists.

    Returns:
    list of lists: The modified nested list with the specified element inserted.
    """
    for sublist in nested_list:
        # Iterate over the sublist in reverse order to avoid index shift issues
        for i in range(len(sublist) - 1, -1, -1):
            sublist.insert(i, element)
    return nested_list
