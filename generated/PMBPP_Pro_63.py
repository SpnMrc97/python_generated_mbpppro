from collections import ChainMap

def merge_dictionaries_list(dict_list):
    """
    Merges a list of dictionaries into a single dictionary.

    :param dict_list: List of dictionaries to merge
    :return: A single dictionary containing all key-value pairs from the input dictionaries
    """
    # Using ChainMap to merge dictionaries
    merged_dict = dict(ChainMap(*dict_list))
    return merged_dict
