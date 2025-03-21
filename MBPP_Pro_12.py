def remove_dirty_chars_from_list(strings, second_strings):
    result = []
    
    # Iterate over both lists simultaneously using zip
    for s1, s2 in zip(strings, second_strings):
        # Create a set of characters to remove
        chars_to_remove = set(s2)
        
        # Build the cleaned string by excluding characters present in chars_to_remove
        cleaned_string = ''.join(c for c in s1 if c not in chars_to_remove)
        
        # Add the cleaned string to the result list
        result.append(cleaned_string)
    
    return result
