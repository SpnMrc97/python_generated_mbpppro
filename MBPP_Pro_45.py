def is_undulating(number):
    str_num = str(number)
    if len(str_num) < 2:
        return False
    first_digit, second_digit = str_num[0], str_num[1]
    if first_digit == second_digit:
        return False
    for i in range(2, len(str_num)):
        if str_num[i] == str_num[i - 1] or str_num[i] not in {first_digit, second_digit}:
            return False
    return True

def longest_undulating_subsequence(numbers):
    undulating_numbers = [num for num in numbers if is_undulating(num)]
    
    # If no undulating numbers found, return an empty list
    if not undulating_numbers:
        return []
    
    # Use dynamic programming to find the longest increasing subsequence
    n = len(undulating_numbers)
    dp = [1] * n
    prev_index = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if undulating_numbers[j] < undulating_numbers[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev_index[i] = j

    # Find the index of the maximum value in dp
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the longest subsequence
    longest_subsequence = []
    while max_index != -1:
        longest_subsequence.append(undulating_numbers[max_index])
        max_index = prev_index[max_index]

    return longest_subsequence[::-1]  # Reverse to get the correct order
