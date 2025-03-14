def count_same_items_in_lists(list_of_lists):
    if not list_of_lists or not all(list_of_lists):
        return 0

    # Transpose the list of lists to group elements by their positions
    transposed_lists = zip(*list_of_lists)

    identical_count = 0

    # Iterate through each group of elements by position
    for group in transposed_lists:
        # Check if all elements in the group are the same
        if all(element == group[0] for element in group):
            identical_count += 1

    return identical_count
