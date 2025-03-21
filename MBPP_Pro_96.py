def total_occurrence(lst):
    count = 0
    for string in lst:
        count += string.count('std')
    return count
