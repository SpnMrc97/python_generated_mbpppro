def sum_of_square_sums(lst):
    def sum_of_squares_of_first_n_odds(n):
        # Calculate the sum of squares of the first n odd numbers
        sum_of_squares = 0
        for i in range(n):
            odd_number = 2 * i + 1  # Generate the ith odd number
            sum_of_squares += odd_number ** 2
        return sum_of_squares
    
    total_sum = 0
    for n in lst:
        total_sum += sum_of_squares_of_first_n_odds(n)
    
    return total_sum
