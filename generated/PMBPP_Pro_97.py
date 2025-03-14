def total_perimeter_pentagons(side_lengths):
    """
    Calculate the total perimeter of multiple regular pentagons.

    Parameters:
    side_lengths (list of float): A list containing the side lengths of the pentagons.

    Returns:
    float: The total perimeter of all pentagons combined.
    """
    total_perimeter = 0.0
    for side_length in side_lengths:
        # Each regular pentagon has 5 sides
        perimeter = 5 * side_length
        total_perimeter += perimeter
    return total_perimeter
