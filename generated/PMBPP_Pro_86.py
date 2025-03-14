def reverse_vowels_in_words(lst):
    def reverse_vowels(word):
        vowels = 'aeiouAEIOU'
        word_list = list(word)
        # List to hold the indices and vowels found in the word
        vowel_positions = [(i, char) for i, char in enumerate(word_list) if char in vowels]

        # Reverse the vowels in the word
        for i in range(len(vowel_positions) // 2):
            # Swap the vowels
            left_index, left_vowel = vowel_positions[i]
            right_index, right_vowel = vowel_positions[-(i + 1)]
            word_list[left_index], word_list[right_index] = right_vowel, left_vowel

        return ''.join(word_list)

    return [reverse_vowels(word) for word in lst]
