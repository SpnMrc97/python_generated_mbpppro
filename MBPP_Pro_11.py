def total_square_perimeter(side_lengths):
    total_perimeter = 0
    for side in side_lengths:
        total_perimeter += 4 * side
    return total_perimeter
