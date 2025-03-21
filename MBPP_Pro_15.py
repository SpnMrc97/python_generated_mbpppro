def find_numbers_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        # Reverse the digits of the number
        reversed_num = int(str(num)[::-1])
        
        # Check if the number is one less than twice its reverse
        if num == 2 * reversed_num - 1:
            result.append(num)
    
    return result
