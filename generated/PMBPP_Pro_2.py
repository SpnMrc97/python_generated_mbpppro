def remove_odd_values_from_list(list_of_strings):
    """
    Remove characters with odd index values from each string in the given list of strings.
    
    Parameters:
    list_of_strings (list): A list of strings to process.

    Returns:
    list: A new list of strings with odd-indexed characters removed from each string.
    """
    result = []
    for string in list_of_strings:
        # Use slicing to keep only characters with even indexes
        even_indexed_string = string[::2]
        result.append(even_indexed_string)
    return result
