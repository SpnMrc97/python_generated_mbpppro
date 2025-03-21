def is_monotonic(array):
    if len(array) <= 1:
        return True
    
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
        if array[i] < array[i - 1]:
            increasing = False

    return increasing or decreasing

def count_monotonic_arrays(arrays):
    count = 0
    for array in arrays:
        if is_monotonic(array):
            count += 1
    return count
