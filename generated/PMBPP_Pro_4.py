def replace_and_concatenate(str_list, char):
    """
    Replace all spaces in each string of the list with the given character
    and concatenate all modified strings into a single string.
    
    Parameters:
    str_list (list of str): A list of strings to be processed.
    char (str): A character to replace spaces with.
    
    Returns:
    str: The concatenated string after replacements.
    """
    if not isinstance(str_list, list) or not isinstance(char, str) or len(char) != 1:
        raise ValueError("Invalid input: str_list must be a list of strings and char must be a single character string.")

    modified_strings = [s.replace(' ', char) for s in str_list]
    concatenated_result = ''.join(modified_strings)
    
    return concatenated_result
