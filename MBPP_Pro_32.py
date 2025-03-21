def find_all_tuples(test_cases, K):
    result = []
    
    # Iterate over each test case
    for test_case in test_cases:
        # Iterate over each tuple in the test case
        for tup in test_case:
            # Check if all elements in the tuple are divisible by K
            if all(element % K == 0 for element in tup):
                result.append(tup)
    
    return result
