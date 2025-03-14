def sum_negativenums(nums_list):
    """
    Calculate the sum of all negative numbers in each sublist and return a list of these sums.

    :param nums_list: List of lists containing numbers.
    :return: List containing the sum of negative numbers for each sublist.
    """
    negative_sums = []
    for sublist in nums_list:
        # Calculate the sum of negative numbers in the current sublist
        negative_sum = sum(num for num in sublist if num < 0)
        # Append the result to the negative_sums list
        negative_sums.append(negative_sum)
    
    return negative_sums
