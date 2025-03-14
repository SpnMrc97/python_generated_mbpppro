def sum_of_sums_even_and_even_index(arr_of_arrs):
    total_sum = 0
    for sublist in arr_of_arrs:
        sublist_sum = 0
        for index, value in enumerate(sublist):
            if index % 2 == 0 and value % 2 == 0:
                sublist_sum += value
        total_sum += sublist_sum
    return total_sum
