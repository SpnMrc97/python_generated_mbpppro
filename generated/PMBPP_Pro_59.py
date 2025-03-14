def three_odd_length_words(words):
    """
    Determine if a list of words contains exactly three words with odd lengths.

    Args:
    words (list of str): A list of words to check.

    Returns:
    bool: True if there are exactly three words with odd lengths, False otherwise.
    """
    odd_length_count = sum(1 for word in words if len(word) % 2 != 0)
    return odd_length_count == 3
