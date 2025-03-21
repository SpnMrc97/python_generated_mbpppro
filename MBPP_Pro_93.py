def total_frequency(list_of_lists, x):
    count = 0
    for sublist in list_of_lists:
        count += sublist.count(x)
    return count
