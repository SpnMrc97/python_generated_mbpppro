def centered_hexagonal_number(n):
    return 3 * n * (n - 1) + 1

def sum_centered_hexagonal_numbers(points):
    total_sum = 0
    for point in points:
        # Assuming 'point' corresponds to 'n' in the centered hexagonal number formula.
        # If 'point' needs to be mapped differently, adjust accordingly.
        total_sum += centered_hexagonal_number(point)
    return total_sum
