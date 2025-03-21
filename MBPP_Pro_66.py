def find_unique_in_sorted_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        # Check if the mid is even or odd to decide the direction
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
    
    return arr[left]

def find_all_unique_elements(arrays):
    unique_elements = []
    for arr in arrays:
        unique_element = find_unique_in_sorted_array(arr)
        unique_elements.append(unique_element)
    
    return unique_elements
