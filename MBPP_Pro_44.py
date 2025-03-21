def find_substring_in_lists(list_of_lists, sub_str):
    # Initialize an empty list to store the indices of lists containing the substring
    indices = []

    # Iterate over the list of lists with their indices
    for i, sublist in enumerate(list_of_lists):
        # Check if the substring is present in any of the strings in the current sublist
        if any(sub_str in string for string in sublist):
            # If found, append the index of the sublist to the indices list
            indices.append(i)
            
    # Return the list of indices
    return indices
