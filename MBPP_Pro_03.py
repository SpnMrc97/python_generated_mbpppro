def count_pairs_differ_at_one_bit_pos(nums):
    # Initialize a counter for the number of valid pairs
    count = 0
    
    # Iterate over all possible pairs in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Calculate XOR of the pair
            xor_result = nums[i] ^ nums[j]
            
            # Check if the result is a power of two (i.e., only one bit is set)
            # A number is a power of two if it has only one bit set, i.e., (xor_result & (xor_result - 1)) == 0
            if xor_result != 0 and (xor_result & (xor_result - 1)) == 0:
                count += 1
    
    return count
