def get_max_length_tuples(input_list):
    if not input_list:
        return []

    # Find the maximum length of tuples in the input list
    max_length = max(len(t) for t in input_list)

    # Filter and return the list of tuples that have the maximum length
    return [t for t in input_list if len(t) == max_length]
