def convert_and_concatenate_binary(decimal_list):
    # Convert each decimal number to a binary string, remove the '0b' prefix
    binary_strings = [bin(num)[2:] for num in decimal_list]
    
    # Concatenate all binary strings together
    concatenated_binary = ''.join(binary_strings)
    
    # Remove leading zeros from the concatenated result
    result = concatenated_binary.lstrip('0')
    
    # Return the final result, or '0' if the result is empty
    return result if result else '0'
