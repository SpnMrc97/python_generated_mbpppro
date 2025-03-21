from operator import itemgetter

def index_minimum(test_list):
    result = []
    for sublist in test_list:
        if not sublist:  # Check if the sublist is empty
            continue
        # Find the tuple with the smallest second value using min with itemgetter
        min_tuple = min(sublist, key=itemgetter(1))
        # Append the first value of that tuple to the result list
        result.append(min_tuple[0])
    return result
