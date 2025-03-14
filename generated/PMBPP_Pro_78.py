def sum_tuples_to_int(tuples_list):
    """
    Convert each tuple of positive integers into a single integer by treating the elements as digits,
    and sum all these integers together.

    Parameters:
    tuples_list (list of tuples): A list where each element is a tuple of positive integers.

    Returns:
    int: The sum of all integers formed from the tuples.
    """
    total_sum = 0

    for tpl in tuples_list:
        # Convert the tuple into a single integer
        number_str = ''.join(map(str, tpl))
        number = int(number_str)
        # Add the integer to the total sum
        total_sum += number

    return total_sum
