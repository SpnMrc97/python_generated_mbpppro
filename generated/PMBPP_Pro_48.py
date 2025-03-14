def total_sum_of_digits(lists_of_nums):
    total_sum = 0
    for sublist in lists_of_nums:
        for number in sublist:
            # Convert the number to a string to iterate over each digit
            digits = str(abs(number))
            # Sum the digits of the number
            sum_of_digits = sum(int(digit) for digit in digits)
            # Add to the total sum
            total_sum += sum_of_digits
    return total_sum
