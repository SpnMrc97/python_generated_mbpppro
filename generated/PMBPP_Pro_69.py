from functools import reduce
from operator import mul

def sum_of_multiplied_nums(list_of_lists):
    total_sum = 0
    for sublist in list_of_lists:
        if not sublist:
            continue  # Skip empty sublists to avoid division by zero
        # Calculate the product of all numbers in the sublist
        product = reduce(mul, sublist, 1)
        # Divide the product by the length of the sublist
        result = product / len(sublist)
        # Add the result to the total sum
        total_sum += result
    return total_sum
