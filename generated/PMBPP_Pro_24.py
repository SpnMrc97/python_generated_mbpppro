def even_Power_Sum_List(lst):
    def sum_of_even_powers(n):
        # Generate the first n even natural numbers
        even_numbers = [2 * i for i in range(1, n + 1)]
        # Calculate the sum of their fifth powers
        return sum(even ** 5 for even in even_numbers)
    
    # Compute the sum of even powers for each n in the list
    result = [sum_of_even_powers(n) for n in lst]
    
    return result
