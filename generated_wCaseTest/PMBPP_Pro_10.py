def max_sum_2d(arr_2d):
    def max_bitonic_sum(arr):
        n = len(arr)
        
        # Initialize the increasing and decreasing subsequence sum arrays
        inc = [0] * n
        dec = [0] * n
        
        # Fill increasing subsequence sum array
        for i in range(n):
            inc[i] = arr[i]
            for j in range(i):
                if arr[j] < arr[i]:
                    inc[i] = max(inc[i], inc[j] + arr[i])
        
        # Fill decreasing subsequence sum array
        for i in range(n-1, -1, -1):
            dec[i] = arr[i]
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    dec[i] = max(dec[i], dec[j] + arr[i])
        
        # Calculate the maximum bitonic sum for this row
        max_bitonic = 0
        for i in range(n):
            max_bitonic = max(max_bitonic, inc[i] + dec[i] - arr[i])
        
        return max_bitonic
    
    total_max_bitonic_sum = 0
    
    # Compute the maximum bitonic sum for each row and add to the total
    for row in arr_2d:
        total_max_bitonic_sum += max_bitonic_sum(row)
    
    return total_max_bitonic_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert max_sum_2d([[1, 15, 51, 45, 33, 100, 12, 18, 9]]) == 194
assert max_sum_2d([[80, 60, 30, 40, 20, 10], [1, 15, 51, 45, 33, 100, 12, 18, 9]]) == 404
assert max_sum_2d([[1, 2, 3, 4, 5, 4, 3, 2, 1], [5, 4, 3, 2, 1, 2, 3, 4, 5]]) == 40

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)