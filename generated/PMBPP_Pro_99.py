def is_majority_in_arrays(arrays, lengths, target):
    """
    Determine if the target element is the majority element in each of the given sorted arrays.

    Parameters:
    - arrays (list of list of int): List of sorted arrays.
    - lengths (list of int): List of lengths of each array.
    - target (int): The target element to check.

    Returns:
    - list of bool: A list of boolean values indicating whether the target is the majority element in each array.
    """
    results = []

    for i, array in enumerate(arrays):
        n = lengths[i]
        # Calculate the majority count needed
        majority_count = n // 2

        # Check if target is the majority element
        # Since the array is sorted, count occurrences of target using binary search
        first_index = binary_search_first(array, target, 0, n - 1)
        
        if first_index == -1:
            # Target not present in the array
            results.append(False)
        else:
            # Calculate the last index of the target
            last_index = binary_search_last(array, target, 0, n - 1)
            count = last_index - first_index + 1
            results.append(count > majority_count)

    return results

def binary_search_first(array, target, low, high):
    """
    Find the first occurrence of target in array using binary search.
    """
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            result = mid
            high = mid - 1  # Keep searching to the left
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def binary_search_last(array, target, low, high):
    """
    Find the last occurrence of target in array using binary search.
    """
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            result = mid
            low = mid + 1  # Keep searching to the right
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
