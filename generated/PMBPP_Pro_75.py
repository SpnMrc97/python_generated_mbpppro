import heapq

def merge_sorted_lists(lists):
    # Initialize a heap
    min_heap = []
    
    # Add the first element of each list along with its list index and element index to the heap
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # Check if the list is not empty
            heapq.heappush(min_heap, (sorted_list[0], i, 0))
    
    # Initialize the result list
    merged_list = []
    
    # Process the heap until it is empty
    while min_heap:
        # Extract the smallest item
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Check if there is a next element in the same list
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
    
    return merged_list
