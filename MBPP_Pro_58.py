def total_count(lists):
    count = 0
    for lst in lists:
        for item in lst:
            if item is True:
                count += 1
    return count
