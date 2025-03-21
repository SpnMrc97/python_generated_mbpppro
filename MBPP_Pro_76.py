def reverse_vowels_in_words(lst):
    def reverse_vowels(word):
        vowels = "aeiouAEIOU"
        word_chars = list(word)
        i, j = 0, len(word_chars) - 1
        
        # Use two-pointer technique to reverse vowels in the word
        while i < j:
            if word_chars[i] not in vowels:
                i += 1
            elif word_chars[j] not in vowels:
                j -= 1
            else:
                # Swap the vowels
                word_chars[i], word_chars[j] = word_chars[j], word_chars[i]
                i += 1
                j -= 1
        
        return ''.join(word_chars)
    
    # Apply the reverse_vowels function to each word in the list
    return [reverse_vowels(word) for word in lst]
