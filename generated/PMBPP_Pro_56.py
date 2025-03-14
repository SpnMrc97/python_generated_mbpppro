def count_pairs_differ_at_one_bit_pos(nums):
    """
    Count the number of pairs of integers in the list that differ at exactly one bit position.

    Args:
    nums (List[int]): List of integers.

    Returns:
    int: The number of pairs that differ at exactly one bit position.
    """
    def is_power_of_two(n):
        """Check if a number is a power of two."""
        return n > 0 and (n & (n - 1)) == 0

    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if is_power_of_two(nums[i] ^ nums[j]):
                count += 1

    return count
