def can_partition_divisible_by_11(nums):
    total_sum = sum(nums)
    
    # If total_sum is not divisible by 22, we cannot partition it into two subsets
    # each having a sum which is a multiple of 11.
    if total_sum % 22 != 0:
        return False
    
    # We need to find if there exists a subset with sum = total_sum // 2
    target = total_sum // 2
    
    # Initialize a set to store sums we can achieve with subsets of nums
    achievable_sums = {0}
    
    for num in nums:
        # Update achievable_sums with current number
        new_sums = set()
        for s in achievable_sums:
            new_sum = s + num
            new_sums.add(new_sum)
        achievable_sums.update(new_sums)
        
        # Check if target is achievable
        if target in achievable_sums:
            return True
    
    return False
