def swap_all_numbers(tuples_list):
    """
    Swaps the two numbers in each tuple within a list of tuples.

    Parameters:
    tuples_list (list of tuples): A list where each element is a tuple containing two numbers.

    Returns:
    list of tuples: A new list of tuples with the numbers in each tuple swapped.
    """
    # List comprehension to swap numbers in each tuple
    swapped_tuples = [(b, a) for a, b in tuples_list]
    return swapped_tuples
