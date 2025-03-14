def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def common_divisors_sum(a, b):
    """Finds the sum of common divisors of two numbers."""
    gcd_value = gcd(a, b)
    divisors_sum = 0
    for i in range(1, gcd_value + 1):
        if gcd_value % i == 0:
            divisors_sum += i
    return divisors_sum

def sum_of_sums_of_common_divisors(pairs):
    """Calculates the sum of the sums of common divisors for each pair in the list."""
    total_sum = 0
    for a, b in pairs:
        total_sum += common_divisors_sum(a, b)
    return total_sum
