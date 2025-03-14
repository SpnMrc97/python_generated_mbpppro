def sum_ascii_values(s):
    """
    Calculate the sum of the ASCII values of all characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII values of the characters in the string.
    """
    return sum(ord(char) for char in s)
