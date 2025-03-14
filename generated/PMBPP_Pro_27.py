def multi_dict_filter(dict_list, n):
    """
    Filters a list of dictionaries to only include entries with values >= n.

    :param dict_list: List[Dict] - A list of dictionaries with comparable values.
    :param n: int - The threshold value to filter dictionary entries.
    :return: Tuple[List[Dict], int] - A tuple containing the filtered list of dictionaries
             and the total count of filtered entries.
    """
    filtered_dict_list = []
    total_filtered_count = 0

    for d in dict_list:
        # Create a filtered dictionary with values >= n
        filtered_dict = {key: value for key, value in d.items() if value >= n}
        
        # Count the number of entries in this filtered dictionary
        total_filtered_count += len(filtered_dict)
        
        # Append the filtered dictionary to the result list
        filtered_dict_list.append(filtered_dict)

    return filtered_dict_list, total_filtered_count
