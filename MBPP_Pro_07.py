def remove_all_occurrences(lst, ch):
    # Ensure the input is a single character
    if len(ch) != 1:
        raise ValueError("The parameter 'ch' should be a single character.")

    # Create a new list to store the modified strings
    result = []

    for string in lst:
        # Remove all occurrences of the character 'ch' from the current string
        modified_string = string.replace(ch, '')
        # Append the modified string to the result list
        result.append(modified_string)

    return result
