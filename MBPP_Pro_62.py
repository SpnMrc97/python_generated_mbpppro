def common_elements_count(nested_lists):
    if not nested_lists:
        return {}

    # Find the common elements across all nested lists
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)

    # Initialize a dictionary to store the counts of each common element
    common_counts = {element: [] for element in common_elements}

    # Count the occurrences of each common element in each nested list
    for lst in nested_lists:
        for element in common_elements:
            count = lst.count(element)
            common_counts[element].append(count)

    return common_counts
