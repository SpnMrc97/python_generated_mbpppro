def smallest_in_sublists(list_of_lists):
    if not list_of_lists or not all(isinstance(sublist, list) and sublist for sublist in list_of_lists):
        raise ValueError("Input must be a list of non-empty lists.")

    smallest_numbers = [min(sublist) for sublist in list_of_lists]
    return min(smallest_numbers)
