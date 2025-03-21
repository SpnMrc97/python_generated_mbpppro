def three_odd_length_words(words):
    # Initialize a counter for words with odd lengths
    odd_length_count = 0
    
    # Iterate over the list of words
    for word in words:
        # Check if the length of the word is odd
        if len(word) % 2 != 0:
            # Increment the counter
            odd_length_count += 1
            
        # Early exit if more than three odd-length words are found
        if odd_length_count > 3:
            return False
    
    # Return True if exactly three words have odd lengths, otherwise False
    return odd_length_count == 3
