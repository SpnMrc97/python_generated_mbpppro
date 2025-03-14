def combine_nested_dictionaries(list_of_lists):
    """
    Combine multiple sets of three lists into a single nested dictionary.

    Each set consists of three lists: keys_list, subkeys_list, and values_list.
    The function creates a nested dictionary structure where each key from
    keys_list maps to a dictionary constructed from subkeys_list and values_list.
    If there are conflicting keys, the latest occurrence overwrites the previous one.

    :param list_of_lists: A list containing multiple sets of three lists.
                          Each set is a tuple or list: (keys_list, subkeys_list, values_list).
    :return: A single nested dictionary.
    """
    combined_dict = {}

    for keys_list, subkeys_list, values_list in list_of_lists:
        for key, subkey, value in zip(keys_list, subkeys_list, values_list):
            if key not in combined_dict:
                combined_dict[key] = {}
            combined_dict[key][subkey] = value

    return combined_dict
