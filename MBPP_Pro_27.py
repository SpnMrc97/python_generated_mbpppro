def is_sequence_of_sublists(list_of_lists, sequence_of_sublists):
    # Get the lengths of both lists
    n = len(list_of_lists)
    m = len(sequence_of_sublists)
    
    # If the sequence of sublists is longer than the list of lists, return False
    if m > n:
        return False
    
    # Iterate through the list_of_lists
    for i in range(n - m + 1):
        # Check if the slice from i to i+m in list_of_lists matches sequence_of_sublists
        if list_of_lists[i:i+m] == sequence_of_sublists:
            return True
    
    # If no matching sequence is found, return False
    return False
