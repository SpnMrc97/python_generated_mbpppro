def shared_elements(lists):
    if not lists:
        return []  # Return an empty list if the input is empty

    # Start by converting the first list into a set
    shared_set = set(lists[0])

    # Iterate through the remaining lists and intersect with the shared set
    for lst in lists[1:]:
        shared_set.intersection_update(lst)

    # Convert the resulting set back to a list
    return list(shared_set)
