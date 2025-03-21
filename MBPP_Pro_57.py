def sort_nested_lists(input_list):
    # Step 1: Sort each sublist
    for sublist in input_list:
        sublist.sort()

    # Step 2: Sort the list of lists
    # Use a lambda function to sort by the first element, then second, and so forth
    input_list.sort(key=lambda sublist: tuple(sublist))
    
    return input_list
