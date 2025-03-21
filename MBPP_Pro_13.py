def find_duplicate_arrays(arrays):
    duplicate_indices = []

    for index, array in enumerate(arrays):
        # Convert the array to a set and compare its length to the original array
        if len(array) != len(set(array)):
            duplicate_indices.append(index)

    return duplicate_indices
