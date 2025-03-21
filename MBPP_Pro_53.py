def is_palindrome(num):
    return str(num) == str(num)[::-1]

def next_smallest_palindrome(num):
    num += 1  # Start checking from the next number
    while not is_palindrome(num):
        num += 1
    return num

def sum_of_next_smallest_palindromes(nums):
    if not nums:
        return 0
    
    total_sum = 0
    for num in nums:
        total_sum += next_smallest_palindrome(num)
    
    return total_sum
