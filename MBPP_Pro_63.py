def count_and_extract_integers(strings):
    count = 0
    integer_list = []
    
    for s in strings:
        try:
            # Try to convert the string to an integer
            num = int(s)
            # If successful, increment the count and add to the list
            count += 1
            integer_list.append(num)
        except ValueError:
            # If conversion fails, continue to the next string
            continue
    
    return count, integer_list
