def count_divisors(n):
    if n < 1:
        return 0

    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def total_divisors(lst):
    total = 0
    for number in lst:
        total += count_divisors(number)
    return total
