def smallest_power_of_2_for_sum(lst):
    if not lst:
        return 0

    total_sum = sum(lst)
    power_of_2 = 1

    while power_of_2 < total_sum:
        power_of_2 *= 2

    return power_of_2
