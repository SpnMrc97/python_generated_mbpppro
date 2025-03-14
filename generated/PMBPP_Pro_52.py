def sum_of_flattened_lists(list_of_lists):
    def flatten(lst):
        """ Helper function to flatten a nested list. """
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    total_sum = 0
    for sublist in list_of_lists:
        flat_list = list(flatten(sublist))
        total_sum += sum(flat_list)
    
    return total_sum
