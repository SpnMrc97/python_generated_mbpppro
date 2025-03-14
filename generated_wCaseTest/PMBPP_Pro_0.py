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

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert first_n_non_primes(1, 10, 3) == [1, 4, 6]
assert first_n_non_primes(10, 20, 5) == [10, 12, 14, 15, 16]
assert first_n_non_primes(20, 30, 10) == [20, 21, 22, 24, 25, 26, 27, 28, 30]
assert first_n_non_primes(1, 5, 10) == [1, 4]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)