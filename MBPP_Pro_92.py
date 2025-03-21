def smallest_power_of_2_for_sum(lst):
    if not lst:
        return 0
    
    # Calculate the sum of all integers in the list
    total_sum = sum(lst)
    
    # Find the smallest power of 2 greater than or equal to the sum
    power = 1
    while power < total_sum:
        power *= 2
    
    return power
