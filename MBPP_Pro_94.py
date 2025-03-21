def total_sum_of_ranges(list_of_lists, m, n):
    total_sum = 0

    # Iterate over each sublist in the list of lists
    for sublist in list_of_lists:
        # Calculate the sum of the elements in the sublist from index m to n (inclusive)
        sublist_sum = sum(sublist[m:n+1])
        # Add this sublist_sum to the total_sum
        total_sum += sublist_sum

    return total_sum
