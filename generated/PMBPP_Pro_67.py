def total_divisors(lst):
    def count_divisors(n):
        """Returns the number of divisors of a given integer n."""
        if n <= 0:
            return 0
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count

    total_count = 0
    for number in lst:
        total_count += count_divisors(number)
    
    return total_count
