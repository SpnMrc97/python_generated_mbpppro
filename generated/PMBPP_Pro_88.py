def sum_of_hexagonal_numbers(N):
    """
    Calculate the sum of the first N hexagonal numbers.

    Parameters:
    N (int): The number of hexagonal numbers to sum.

    Returns:
    int: The sum of the first N hexagonal numbers.
    """
    if N < 1:
        raise ValueError("N must be a positive integer")

    hexagonal_sum = sum(n * (2 * n - 1) for n in range(1, N + 1))
    return hexagonal_sum
