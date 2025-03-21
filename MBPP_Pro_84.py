def complex_sort(list_of_lists):
    # Sort each sublist individually
    sorted_sublists = [sorted(sublist) for sublist in list_of_lists]

    # Sort the main list based on the sum of elements in each sublist
    sorted_main_list = sorted(sorted_sublists, key=sum)

    return sorted_main_list
