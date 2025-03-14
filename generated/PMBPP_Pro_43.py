def sum_lucas_numbers(start, k):
    if start < 0 or k < 0:
        raise ValueError("Start and k must be non-negative integers.")
    
    # Initialize the first two Lucas numbers
    lucas_numbers = [2, 1]
    
    # Generate Lucas numbers until we have enough to sum from the 'start' position
    while len(lucas_numbers) < start + k:
        lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])
    
    # Calculate the sum of 'k' Lucas numbers starting from 'start'
    return sum(lucas_numbers[start:start + k])
