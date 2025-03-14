def find_all_unique_elements(arrays):
    from collections import defaultdict
    
    # Dictionary to hold the count of each element
    element_count = defaultdict(int)
    
    # Iterate over each array
    for array in arrays:
        # Iterate over each element in the array
        for element in array:
            # Increment the count of the element
            element_count[element] += 1
    
    # Find and return elements that appear once
    unique_elements = [element for element, count in element_count.items() if count == 1]
    
    return unique_elements
