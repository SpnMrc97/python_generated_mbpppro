from math import comb

def sum_even_binomial_coeffs(numbers):
    results = []
    for n in numbers:
        sum_even_indices = 0
        # Iterate over even indices
        for k in range(0, n + 1, 2):
            sum_even_indices += comb(n, k)
        results.append(sum_even_indices)
    return results
