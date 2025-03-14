def sum_centered_hexagonal_numbers(points):
    def centered_hexagonal_number(n):
        return 3 * n * (n - 1) + 1

    total_sum = 0
    for point in points:
        total_sum += centered_hexagonal_number(point)
    
    return total_sum
