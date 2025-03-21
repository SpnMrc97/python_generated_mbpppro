def total_set_bits(numbers):
    total_bits = 0
    for number in numbers:
        # Convert number to binary and count the '1's
        total_bits += bin(number).count('1')
    return total_bits
