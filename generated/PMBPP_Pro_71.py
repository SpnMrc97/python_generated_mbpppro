def is_palindrome(n):
    """Check if an integer is a palindrome."""
    s = str(n)
    return s == s[::-1]

def next_smallest_palindrome(n):
    """Find the next smallest palindrome greater than the given number."""
    while True:
        n += 1
        if is_palindrome(n):
            return n

def sum_of_next_smallest_palindromes(nums):
    """Calculate the sum of the next smallest palindromes for each number in the list."""
    if not nums:
        return 0

    total = 0
    for num in nums:
        palindrome = next_smallest_palindrome(num)
        total += palindrome
    
    return total
