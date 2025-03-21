def dif_Square_list(lst):
    # Initialize a list to store the results
    results = []
    
    # Iterate over each integer in the input list
    for n in lst:
        # Check if the integer n can be represented as the difference of two squares
        if n % 4 == 0 or n % 4 == 1:
            results.append(True)
        else:
            results.append(False)
    
    return results
