def max_sum_of_series(lst):
    if not lst:
        return 0
    
    def series_sum(n):
        return n * (n + 1) // 2  # Using integer division as the result is an integer

    max_sum = 0
    for number in lst:
        current_sum = series_sum(number)
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
