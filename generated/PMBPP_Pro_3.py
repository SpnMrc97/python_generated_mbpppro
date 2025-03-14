def max_of_min_of_three(list_of_lists):
    # Check if the input list is not empty
    if not list_of_lists:
        raise ValueError("The input list should not be empty.")
    
    min_values = []
    
    # Iterate over each sublist in the list of lists
    for sublist in list_of_lists:
        # Check if each sublist contains exactly three numbers
        if len(sublist) != 3:
            raise ValueError("Each sublist must contain exactly three numbers.")
        
        # Find the minimum number in the current sublist
        min_value = min(sublist)
        
        # Append the minimum value to the min_values list
        min_values.append(min_value)
    
    # Find and return the maximum of the minimum values
    return max(min_values)
