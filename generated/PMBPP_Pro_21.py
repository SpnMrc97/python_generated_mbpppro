def sum_star_nums(k):
    """
    Calculate the sum of the first k star numbers.

    Parameters:
    k (int): The number of star numbers to sum.

    Returns:
    int: The sum of the first k star numbers.
    """
    if k < 1:
        return 0
    
    total_sum = 0
    for n in range(1, k + 1):
        star_number = 6 * n * (n - 1) + 1
        total_sum += star_number
    
    return total_sum
