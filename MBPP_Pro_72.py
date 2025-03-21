def product_of_list(lst):
    # Initialize the product to 1 (multiplicative identity)
    product = 1
    
    # Iterate over each element in the list
    for num in lst:
        # Multiply the current number to the product
        product *= num
        
    return product
