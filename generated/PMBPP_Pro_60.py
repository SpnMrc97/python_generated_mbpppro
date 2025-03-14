def sum_of_tetrahedral_numbers(k):
    def tetrahedral_number(n):
        """Calculate the n-th tetrahedral number."""
        return n * (n + 1) * (n + 2) // 6
    
    total_sum = 0
    for i in range(1, k + 1):
        total_sum += tetrahedral_number(i)
    
    return total_sum
