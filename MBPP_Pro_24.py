def total_pos_count(lists):
    total_count = 0
    for lst in lists:
        for num in lst:
            if num > 0:
                total_count += 1
    return total_count
