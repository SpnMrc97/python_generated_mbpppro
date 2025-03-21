def find_all_char_long(texts):
    result = []
    for text in texts:
        # Split the text into words
        words = text.split()
        # Filter words that are at least 4 characters long
        long_words = [word for word in words if len(word) >= 4]
        # Append the list of long words to the result
        result.append(long_words)
    return result
