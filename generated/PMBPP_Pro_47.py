def medians_of_triplets(lst):
    """
    This function takes a list of integers and returns a list containing the median of each triplet.
    If the list length is not a multiple of three, the remaining elements are ignored.
    
    :param lst: List of integers
    :return: List of medians of each triplet
    """
    medians = []
    # Process the list in chunks of three
    for i in range(0, len(lst) - len(lst) % 3, 3):
        triplet = lst[i:i+3]
        triplet.sort()  # Sort the triplet
        median = triplet[1]  # The second element is the median after sorting
        medians.append(median)
    return medians
