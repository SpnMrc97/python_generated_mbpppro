def sum_of_multiplied_nums(list_of_lists):
    total_sum = 0
    
    for sublist in list_of_lists:
        if not sublist:  # Check if the sublist is empty
            continue
        
        product = 1
        for num in sublist:
            product *= num
        
        # Divide the product by the length of the sublist
        result = product / len(sublist)
        
        # Add the result to the total sum
        total_sum += result
    
    return total_sum
