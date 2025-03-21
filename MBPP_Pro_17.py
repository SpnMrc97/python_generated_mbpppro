def count_Opposite_Signs(tuples_list):
    count = 0
    for a, b in tuples_list:
        # Check if one is positive and the other is negative
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            count += 1
    return count
