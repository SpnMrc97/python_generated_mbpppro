def max_product_nested_list(nested_list):
    # Initialize the maximum product to a very small number
    max_product = float('-inf')
    
    # Iterate over each sublist
    for sublist in nested_list:
        # Iterate over each tuple in the sublist
        for t in sublist:
            # Calculate the product of the two numbers in the tuple
            product = t[0] * t[1]
            # Calculate the absolute value of the product
            abs_product = abs(product)
            # Update the maximum product if the current absolute product is greater
            if abs_product > max_product:
                max_product = abs_product
    
    return max_product
