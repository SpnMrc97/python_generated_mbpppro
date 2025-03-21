def check_types_in_list(tuple_list):
    result = []
    for tup in tuple_list:
        # Extract the type of the first element in the tuple
        first_type = type(tup[0])
        # Check if all elements in the tuple are of the same type
        same_type = all(isinstance(item, first_type) for item in tup)
        # Append the result (True/False) to the result list
        result.append(same_type)
    return result
