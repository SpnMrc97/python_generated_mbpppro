def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def first_n_non_primes(start, end, N):
    non_primes = []
    
    for num in range(start, end + 1):
        if not is_prime(num):
            non_primes.append(num)
            if len(non_primes) == N:
                break

    return non_primes
