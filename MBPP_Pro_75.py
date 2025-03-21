from collections import defaultdict

def max_occurrences(nums):
    # Initialize a default dictionary to count occurrences
    count_dict = defaultdict(int)
    
    # Count occurrences of each item
    for sublist in nums:
        for item in sublist:
            count_dict[item] += 1
    
    # Determine the maximum occurrence count
    max_count = max(count_dict.values())
    
    # Find all items with the maximum count
    max_items = [item for item, count in count_dict.items() if count == max_count]
    
    # Return the lexicographically smallest item among those with the maximum count
    return min(max_items)
