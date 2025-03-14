def kth_element_in_flattened_array(arr_of_arrs, k):
    """
    Find the k-th element in the flattened version of an array of arrays.

    :param arr_of_arrs: List of lists, where each sublist contains integers
    :param k: 1-based index of the element to find in the flattened list
    :return: The k-th element in the flattened list
    :raises IndexError: If k is out of bounds for the flattened list
    """
    if k < 1:
        raise IndexError("Index k must be 1 or greater.")

    # Flatten the array of arrays
    flattened = [element for sublist in arr_of_arrs for element in sublist]

    # Check if k is within the bounds of the flattened list
    if k > len(flattened):
        raise IndexError("Index k is out of bounds for the flattened list.")

    # Return the k-th element (convert 1-based index to 0-based)
    return flattened[k - 1]
