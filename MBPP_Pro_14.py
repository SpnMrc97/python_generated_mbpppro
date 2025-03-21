def find_first_10_woodall_numbers(start, end):
    woodall_numbers = []
    n = 0
    while len(woodall_numbers) < 10:
        woodall_number = n * (2**n) - 1
        if start <= woodall_number <= end:
            woodall_numbers.append(woodall_number)
        elif woodall_number > end:
            break
        n += 1
    return woodall_numbers
