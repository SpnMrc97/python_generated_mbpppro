def sum_tuples_to_int(tuples_list):
    total_sum = 0
    for t in tuples_list:
        # Convert each tuple into a single integer
        num_str = ''.join(map(str, t))
        num = int(num_str)
        # Add the integer to the total sum
        total_sum += num
    return total_sum
