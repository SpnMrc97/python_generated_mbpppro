def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

def sum_of_flattened_lists(list_of_lists):
    total_sum = 0
    for sublist in list_of_lists:
        flattened_sublist = flatten(sublist)
        total_sum += sum(flattened_sublist)
    return total_sum
