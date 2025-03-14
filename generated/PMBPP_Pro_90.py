def deep_extract_singly(nested_list):
    """
    Flattens a deeply nested list into a single set of numbers.

    :param nested_list: List containing numbers and/or other lists
    :return: A set of numbers extracted from the nested list
    """
    def flatten_helper(current_list):
        for item in current_list:
            if isinstance(item, list):
                yield from flatten_helper(item)
            else:
                yield item

    return set(flatten_helper(nested_list))
