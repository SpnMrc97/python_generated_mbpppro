def max_sub_array_sum_repeated_multiple(arrays, ks):
    def max_sub_array_sum_k_times(array, k):
        # Calculate the maximum subarray sum for the original array using Kadane's algorithm
        max_ending_here = max_so_far = array[0]
        for x in array[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        
        if k == 1:
            return max_so_far

        # Calculate sum of the entire array
        array_sum = sum(array)
        
        # Calculate the maximum prefix sum
        max_prefix_sum = current_prefix_sum = 0
        for x in array:
            current_prefix_sum += x
            max_prefix_sum = max(max_prefix_sum, current_prefix_sum)
        
        # Calculate the maximum suffix sum
        max_suffix_sum = current_suffix_sum = 0
        for x in reversed(array):
            current_suffix_sum += x
            max_suffix_sum = max(max_suffix_sum, current_suffix_sum)
        
        # If the array sum is positive, consider the middle k-2 arrays
        if array_sum > 0:
            max_so_far = max(max_so_far, max_prefix_sum + max_suffix_sum + array_sum * (k - 2))
        else:
            max_so_far = max(max_so_far, max_prefix_sum + max_suffix_sum)
        
        return max_so_far

    # Initialize the maximum sum among all modified arrays
    max_sum = float('-inf')
    
    # Iterate over each array and its corresponding k
    for array, k in zip(arrays, ks):
        max_sum = max(max_sum, max_sub_array_sum_k_times(array, k))
    
    return max_sum
