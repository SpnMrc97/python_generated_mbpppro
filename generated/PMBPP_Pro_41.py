def find_max_in_tuples(tuples_list):
    """
    Finds the maximum value in a list of tuples where each tuple contains two numbers.
    
    Parameters:
    tuples_list (list of tuple): A list of tuples, each containing two numbers.
    
    Returns:
    int or float: The maximum value found across all tuples.
    """
    if not tuples_list:
        raise ValueError("The input list is empty")

    # Initialize max_value with the smallest possible value
    max_value = float('-inf')
    
    for tuple_pair in tuples_list:
        # Ensure each item in the list is a tuple with two numbers
        if not isinstance(tuple_pair, tuple) or len(tuple_pair) != 2:
            raise ValueError("Each item in the list must be a tuple with exactly two numbers")
        
        for number in tuple_pair:
            if not isinstance(number, (int, float)):
                raise ValueError("Each element in the tuple must be a number")
            
            # Update max_value if the current number is greater
            if number > max_value:
                max_value = number
    
    return max_value
