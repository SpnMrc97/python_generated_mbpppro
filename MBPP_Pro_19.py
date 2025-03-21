def count_substrings(strings):
    total_count = 0

    # Helper function to calculate the sum of digits in a string
    def sum_of_digits(substring):
        return sum(int(char) for char in substring if char.isdigit())

    for s in strings:
        n = len(s)
        # Iterate over all possible substrings
        for start in range(n):
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                # Check if the sum of digits equals the length of the substring
                if sum_of_digits(substring) == len(substring):
                    total_count += 1

    return total_count
