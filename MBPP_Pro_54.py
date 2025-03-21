def kth_element_in_flattened_array(arr_of_arrs, k):
    # Flatten the array of arrays
    flattened_array = [element for sub_array in arr_of_arrs for element in sub_array]
    
    # Check if k is within the valid range
    if k < 1 or k > len(flattened_array):
        raise IndexError("k is out of the bounds of the flattened array")
    
    # Return the kth element using 1-based indexing (subtract 1 for 0-based index)
    return flattened_array[k - 1]
