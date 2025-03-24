def find_max_difference(binary_strings):
    # Step 1: Concatenate all binary strings
    concatenated_string = ''.join(binary_strings)

    # Step 2: Transform the binary string to an array of +1 and -1
    # +1 for '0', -1 for '1'
    transformed_array = [1 if char == '0' else -1 for char in concatenated_string]

    # Step 3: Use modified Kadane's algorithm to find the maximum sum subarray
    max_diff = 0
    current_sum = 0

    for value in transformed_array:
        current_sum += value
        if current_sum > max_diff:
            max_diff = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_diff
