def sum_of_proper_divisors(n):
    if n < 2:
        return 0
    total = 1  # start with 1 because it's a proper divisor of any number
    sqrt_n = int(n**0.5)
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    
    return total

def is_amicable(a, b):
    return a != b and sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a

def sum_amicable_numbers_in_ranges(ranges):
    amicable_numbers = set()
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if num not in amicable_numbers:  # Avoid duplicate checks
                partner = sum_of_proper_divisors(num)
                if partner > num and partner <= end and is_amicable(num, partner):
                    amicable_numbers.add(num)
                    amicable_numbers.add(partner)
    
    return sum(amicable_numbers)
