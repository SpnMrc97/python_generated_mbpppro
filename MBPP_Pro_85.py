def count_same_items_in_lists(list_of_lists):
    if not list_of_lists or not list_of_lists[0]:
        # If the list of lists is empty or the first list is empty, return 0.
        return 0
    
    # Get the number of lists
    num_lists = len(list_of_lists)
    # Get the length of the first list (assuming all lists are of the same length)
    length_of_lists = len(list_of_lists[0])
    
    # Initialize a counter for identical items
    identical_count = 0

    # Iterate over each index position
    for i in range(length_of_lists):
        # Take the item from the first list as reference
        reference_item = list_of_lists[0][i]
        
        # Check if all lists have the same item at position i
        if all(list_of_lists[j][i] == reference_item for j in range(num_lists)):
            identical_count += 1

    return identical_count
