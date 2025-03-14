def sort_nested_lists(input_list):
    """
    Sort each sublist and then sort the entire list of lists by the first element
    of each sublist. If two sublists have the same first element, sort them by their
    second element, and so on.

    Parameters:
    input_list (list of lists): A list where each element is a list of strings.

    Returns:
    list of lists: The sorted list of lists.
    """
    # First, sort each sublist individually
    sorted_sublists = [sorted(sublist) for sublist in input_list]

    # Then, sort the list of lists by the elements within the sublists
    sorted_list = sorted(sorted_sublists, key=lambda x: tuple(x))

    return sorted_list
