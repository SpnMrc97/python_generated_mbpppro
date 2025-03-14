def find_all_tuples(test_cases, K):
    """
    Find all tuples across all test cases that have all elements divisible by a given number K.

    :param test_cases: List of lists of tuples.
    :param K: Integer, the divisor.
    :return: List of tuples that meet the criterion.
    """
    result = []
    for test_case in test_cases:
        for tuple_ in test_case:
            if all(element % K == 0 for element in tuple_):
                result.append(tuple_)
    return result
