def highest_power_of_2_for_sums(lst):
    def highest_power_of_2(n):
        """Helper function to find the highest power of 2 less than or equal to n."""
        power = 1
        while power <= n:
            power <<= 1
        return power >> 1

    max_power_of_2 = 0
    n = len(lst)

    # Iterate over all pairs of distinct elements
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = lst[i] + lst[j]
            power_of_2 = highest_power_of_2(current_sum)
            max_power_of_2 = max(max_power_of_2, power_of_2)

    return max_power_of_2
