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
