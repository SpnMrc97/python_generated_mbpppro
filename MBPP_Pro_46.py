def product_of_powers(tuples_list):
    # Initialize the product as 1
    product = 1
    
    # Iterate over each tuple in the list
    for base, exponent in tuples_list:
        # Calculate the power for each tuple and multiply it to the product
        product *= base ** exponent
    
    return product
