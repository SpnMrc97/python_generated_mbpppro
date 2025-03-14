def sum_of_squares_list(numbers):
    def sum_of_squares_of_first_n_even_numbers(n):
        # Calculate the sum of squares of the first n even natural numbers
        return sum((2 * i) ** 2 for i in range(1, n + 1))
    
    return [sum_of_squares_of_first_n_even_numbers(n) for n in numbers]
