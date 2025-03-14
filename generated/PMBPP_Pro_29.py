def decagonal_number(n):
    """Calculate the n-th decagonal number."""
    return 4 * n ** 2 - 3 * n

def sum_of_decagonal_numbers(lst):
    """Calculate the sum of the first 10 decagonal numbers for each integer in the list."""
    results = []
    for num in lst:
        if num < 0:
            results.append(0)
        else:
            # Calculate the sum of the first 10 decagonal numbers
            sum_decagonal = sum(decagonal_number(i) for i in range(1, 11))
            results.append(sum_decagonal)
    return results
