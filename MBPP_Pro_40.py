def merge_dictionaries_list(dict_list):
    # Initialize an empty dictionary to accumulate the merged result
    merged_dict = {}
    
    # Iterate over each dictionary in the list
    for dictionary in dict_list:
        # Update the merged dictionary with the contents of the current dictionary
        merged_dict.update(dictionary)
    
    return merged_dict
