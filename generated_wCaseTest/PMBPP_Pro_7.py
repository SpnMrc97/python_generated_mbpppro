def count_sequences(m, n):
    # Create a DP table where dp[i][j] represents the number of sequences of length i ending with j
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: for length 1, each number from 1 to m is a valid sequence
    for j in range(1, m + 1):
        dp[1][j] = 1

    # Fill the dp table for sequences of length 2 to n
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            # dp[i][j] is the sum of all dp[i-1][k] where k <= j // 2
            for k in range(1, j // 2 + 1):
                dp[i][j] += dp[i-1][k]

    # The result for sequences of length n is the sum of all dp[n][j] for j = 1 to m
    total_sequences = sum(dp[n][j] for j in range(1, m + 1))
    return total_sequences

def get_total_number_of_sequences_sum(tuples_list):
    total_sum = 0
    for m, n in tuples_list:
        total_sum += count_sequences(m, n)
    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert get_total_number_of_sequences_sum([(5, 3), (10, 2)]) == 27
assert get_total_number_of_sequences_sum([(3, 2), (4, 2), (5, 2)]) == 12
assert get_total_number_of_sequences_sum([(1, 1), (2, 1), (3, 1)]) == 6

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)