def total_char_position(strings):
    total_count = 0
    
    # Iterate through each string in the list
    for string in strings:
        # Enumerate over the string to get both character and 0-based index
        for index, char in enumerate(string):
            # Convert character to lowercase to handle case insensitivity
            char_lower = char.lower()
            # Check if character is a letter
            if 'a' <= char_lower <= 'z':
                # Calculate the 1-based position of the character in the alphabet
                alphabet_position = ord(char_lower) - ord('a') + 1
                # Compare the alphabet position with the 1-based index position
                if alphabet_position == index + 1:
                    total_count += 1
    
    return total_count
