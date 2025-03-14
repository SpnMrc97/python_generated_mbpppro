def can_partition_divisible_by_11(nums):
    total_sum = sum(nums)

    # If the total sum is not divisible by 22, we cannot partition it into two subsets
    # each with a sum divisible by 11.
    if total_sum % 22 != 0:
        return False

    # Target sum for each subset should be total_sum / 2
    # because both subsets need to be divisible by 11 and the total sum is divisible by 22.
    target = total_sum // 2

    # Use dynamic programming to find if there is a subset with sum equal to target
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: zero sum is always possible with empty subset

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    # Check if there's a subset with sum equal to target
    return dp[target]
