def common_elements_count(nested_lists):
    if not nested_lists or not all(nested_lists):
        return {}

    # Find common elements across all nested lists
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)

    # Count occurrences of common elements in each nested list
    common_count_dict = {}
    for element in common_elements:
        counts = [lst.count(element) for lst in nested_lists]
        common_count_dict[element] = counts

    return common_count_dict
