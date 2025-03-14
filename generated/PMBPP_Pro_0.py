def is_prime(number):
    """Helper function to check if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def first_n_non_primes(start, end, N):
    """Function to find the first N non-prime numbers in the range [start, end]."""
    non_primes = []
    for number in range(start, end + 1):
        if not is_prime(number):
            non_primes.append(number)
            if len(non_primes) == N:
                break
    return non_primes
