def sum_negativenums(nums_list):
    result = []  # This will hold the sum of negative numbers for each sublist
    for sublist in nums_list:
        # Filter negative numbers and calculate their sum
        negative_sum = sum(num for num in sublist if num < 0)
        result.append(negative_sum)
    return result
