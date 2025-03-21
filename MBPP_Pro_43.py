def len_longest_word_in_sentences(sentences):
    max_length = 0
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into words
        for word in words:
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
    return max_length
