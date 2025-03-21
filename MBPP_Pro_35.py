def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6

def sum_of_tetrahedral_numbers(k):
    total_sum = 0
    for i in range(1, k + 1):
        total_sum += tetrahedral_number(i)
    return total_sum
