def remove_dirty_chars_from_list(strings, second_strings):
    """
    Given two lists of strings, remove all characters from each string in the first list
    that are present in their corresponding string in the second list. If the lists are
    of different lengths, ignore the extra strings in the longer list.
    
    :param strings: List of strings from which characters will be removed
    :param second_strings: List of strings containing characters to be removed
    :return: A new list of strings with the specified characters removed
    """
    # Find the length up to which both lists have corresponding elements
    min_length = min(len(strings), len(second_strings))
    
    # Create a new list to store the cleaned strings
    cleaned_strings = []
    
    for i in range(min_length):
        # Use a set to store characters to remove for faster lookup
        chars_to_remove = set(second_strings[i])
        
        # Construct the cleaned string by including only characters not in chars_to_remove
        cleaned_string = ''.join(char for char in strings[i] if char not in chars_to_remove)
        
        # Append the cleaned string to the result list
        cleaned_strings.append(cleaned_string)
    
    return cleaned_strings
