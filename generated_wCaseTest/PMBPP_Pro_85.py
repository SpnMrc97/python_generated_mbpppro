def is_magic_square(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False
    
    n = len(matrix)
    magic_sum = sum(matrix[0])

    # Check all rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check all columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    # Check the main diagonal
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    
    # Check the secondary diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True

def count_magic_squares(matrices):
    count = 0
    for matrix in matrices:
        if is_magic_square(matrix):
            count += 1
    return count

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert count_magic_squares([[[2, 7, 6], [9, 5, 1], [4, 3, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[8, 1, 6], [3, 5, 7], [4, 9, 2]]]) == 2
assert count_magic_squares([[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]) == 2
assert count_magic_squares([[[1, 2], [2, 1]], [[1, 1], [1, 1]]]) == 1

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)