def find_all_char_long(texts):
    result = []
    for text in texts:
        words = text.split()
        long_words = [word for word in words if len(word) >= 4]
        result.append(long_words)
    return result
