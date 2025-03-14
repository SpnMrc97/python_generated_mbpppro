def sum_of_divisors(n):
    """Return the sum of proper divisors of n."""
    divisors_sum = 1  # 1 is a proper divisor of every number > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def is_amicable(a):
    """Check if the number a is part of an amicable pair."""
    b = sum_of_divisors(a)
    return a != b and sum_of_divisors(b) == a

def sum_amicable_numbers_in_ranges(ranges):
    """Return the sum of all amicable numbers within the given list of ranges."""
    amicable_numbers = set()
    
    for start, end in ranges:
        for number in range(start, end + 1):
            if number not in amicable_numbers and is_amicable(number):
                pair = sum_of_divisors(number)
                amicable_numbers.add(number)
                amicable_numbers.add(pair)
    
    return sum(amicable_numbers)
