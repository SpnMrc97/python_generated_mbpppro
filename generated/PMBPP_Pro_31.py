def sub_list_of_lists(list_of_lists):
    """Subtracts the second list from the first list element-wise for each sublist in the given list of lists.

    Args:
        list_of_lists (list): A list of lists, where each sublist contains exactly two lists of equal length.

    Returns:
        list: A list containing the result of the element-wise subtraction for each sublist.
    """
    result = []
    for pair in list_of_lists:
        if len(pair) != 2:
            raise ValueError("Each sublist must contain exactly two lists.")
        
        first_list, second_list = pair
        if len(first_list) != len(second_list):
            raise ValueError("The lists in each sublist must be of the same length.")
        
        # Perform element-wise subtraction
        difference = [a - b for a, b in zip(first_list, second_list)]
        result.append(difference)
    
    return result
