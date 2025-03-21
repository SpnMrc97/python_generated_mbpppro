def total_char_position(strings):
    total_count = 0

    for string in strings:
        for index, char in enumerate(string):
            # Convert character to lowercase to make the check case insensitive
            if char.lower() == chr(97 + index):  # 97 is the ASCII value for 'a'
                total_count += 1

    return total_count
