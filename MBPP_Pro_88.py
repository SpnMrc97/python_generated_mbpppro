def remove_elements_from_lists(list_of_lists, exclusion_list):
    # Using list comprehension to filter elements in each sublist
    return [[element for element in sublist if element not in exclusion_list] for sublist in list_of_lists]
