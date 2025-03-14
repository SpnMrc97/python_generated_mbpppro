def find_duplicate_arrays(arrays):
    """
    This function checks each array in a list of arrays for duplicate elements.
    It returns a list of indices of arrays that contain duplicates.

    :param arrays: List of arrays (lists of integers)
    :return: List of indices of arrays with duplicate elements
    """
    duplicate_indices = []

    for index, array in enumerate(arrays):
        if len(array) != len(set(array)):
            duplicate_indices.append(index)

    return duplicate_indices
