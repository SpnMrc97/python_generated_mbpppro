def frequency_nested_lists(nested_list):
    def flatten_list(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten_list(item)
            else:
                yield item

    def calculate_frequency(flat_list):
        frequency_dict = {}
        for item in flat_list:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1
        return frequency_dict

    # Flatten the nested list
    flat_list = list(flatten_list(nested_list))
    
    # Calculate and return the frequency dictionary
    return calculate_frequency(flat_list)
