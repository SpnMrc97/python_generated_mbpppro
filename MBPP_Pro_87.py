def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_solutions(tuples_list):
    solutions = []
    for a, b, n in tuples_list:
        gcd, x0, y0 = extended_gcd(a, b)
        
        if n % gcd != 0:
            solutions.append(None)
        else:
            # Scale the solution to the particular n
            x = x0 * (n // gcd)
            y = y0 * (n // gcd)
            solutions.append((x, y))
    
    return solutions
