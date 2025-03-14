def find_max_difference(binary_strings):
    # Concatenate all binary strings into one
    concatenated_string = ''.join(binary_strings)
    
    # Initialize variables to keep track of the max difference and current difference
    max_difference = 0
    current_difference = 0
    
    for char in concatenated_string:
        # Convert '0' to +1 and '1' to -1 to find max subarray sum
        if char == '0':
            current_difference += 1
        else:  # char == '1'
            current_difference -= 1
        
        # Update max_difference if the current difference is greater
        max_difference = max(max_difference, current_difference)
        
        # If the current difference is negative, reset it to 0
        # This is equivalent to starting a new subarray
        if current_difference < 0:
            current_difference = 0
    
    return max_difference
