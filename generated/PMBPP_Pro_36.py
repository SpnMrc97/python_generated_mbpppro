def find_numbers_in_range(start, end):
    def reverse_number(n):
        return int(str(n)[::-1])

    result = []
    for number in range(start, end + 1):
        reversed_number = reverse_number(number)
        if number == 2 * reversed_number - 1:
            result.append(number)
    
    return result
