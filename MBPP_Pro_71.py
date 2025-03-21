def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def common_divisors_sum(a, b):
    # Find the greatest common divisor
    common_gcd = gcd(a, b)
    
    # Find all divisors of the gcd
    divisors_sum = 0
    for i in range(1, common_gcd + 1):
        if common_gcd % i == 0:
            divisors_sum += i
            
    return divisors_sum

def sum_of_sums_of_common_divisors(pairs):
    total_sum = 0
    for a, b in pairs:
        total_sum += common_divisors_sum(a, b)
    return total_sum
