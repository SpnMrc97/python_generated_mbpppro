def total_perimeter_pentagons(side_lengths):
    # Initialize the total perimeter to zero
    total_perimeter = 0
    
    # Iterate through each side length in the list
    for side in side_lengths:
        # Calculate the perimeter of the current pentagon and add it to the total
        total_perimeter += 5 * side
        
    return total_perimeter
