def is_majority_in_arrays(arrays, lengths, target):
    def find_first_and_last(arr, target):
        # Helper function to find the first and last occurrence of target
        def find_first():
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def find_last():
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        
        first = find_first()
        last = find_last()
        return first, last

    results = []
    for i, arr in enumerate(arrays):
        length = lengths[i]
        first, last = find_first_and_last(arr, target)
        
        # Calculate the number of occurrences of target
        if first <= last and 0 <= first < length and arr[first] == target:
            count = last - first + 1
        else:
            count = 0
        
        # Check if target is a majority element
        is_majority = count > length // 2
        results.append(is_majority)
    
    return results
