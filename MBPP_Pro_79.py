def sum_of_hexagonal_numbers(N):
    """Calculate the sum of the first N hexagonal numbers."""
    total_sum = 0
    for n in range(1, N + 1):
        hexagonal_number = 2 * n * n - n
        total_sum += hexagonal_number
    return total_sum
