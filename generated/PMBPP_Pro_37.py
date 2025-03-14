def sum_of_quotients(operations):
    """
    Calculate the sum of quotients rounded down to the nearest integer
    for each tuple in the list.

    :param operations: List of tuples, where each tuple contains two integers
                       (numerator, denominator).
    :return: Sum of all integer quotients.
    """
    total_sum = 0
    for numerator, denominator in operations:
        if denominator == 0:
            raise ValueError("Division by zero error in operations list.")
        quotient = numerator // denominator
        total_sum += quotient
    return total_sum
