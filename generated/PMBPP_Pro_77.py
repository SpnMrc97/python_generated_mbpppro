def count_and_extract_integers(strings):
    """
    Count how many strings in the list represent integers and return a list of those integers.

    Parameters:
    strings (list of str): The list of strings to evaluate.

    Returns:
    tuple: A tuple containing the count of integer-representing strings and the list of integers.
    """
    integer_list = []
    
    for string in strings:
        try:
            # Attempt to convert string to an integer
            number = int(string)
            integer_list.append(number)
        except ValueError:
            # If conversion fails, continue to the next string
            continue
    
    # Return the count of integers and the list of integers
    return len(integer_list), integer_list
