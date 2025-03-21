def is_magic_square(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False  # Not a square matrix

    # Calculate the sum of the first row to use as a reference
    magic_sum = sum(matrix[0])

    # Check rows and columns
    for i in range(n):
        if sum(matrix[i]) != magic_sum:  # Check row sum
            return False
        if sum(matrix[j][i] for j in range(n)) != magic_sum:  # Check column sum
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_sum:  # Main diagonal
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:  # Other diagonal
        return False

    return True


def count_magic_squares(matrices):
    count = 0
    for matrix in matrices:
        if is_magic_square(matrix):
            count += 1
    return count
