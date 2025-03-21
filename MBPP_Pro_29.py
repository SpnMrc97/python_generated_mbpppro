def sort_list_of_lists(list_of_lists):
    # Sort each sublist individually
    for sublist in list_of_lists:
        sublist.sort()

    # Sort the main list based on the sum of elements in each sublist
    list_of_lists.sort(key=sum)

    return list_of_lists
