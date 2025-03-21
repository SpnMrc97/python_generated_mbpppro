import heapq

def merge_sorted_lists(lists):
    # Create a min-heap
    min_heap = []
    
    # Initialize a list to store the iterators of each list
    iterators = [iter(lst) for lst in lists]
    
    # Add the first element of each list to the heap
    for i, it in enumerate(iterators):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    # Initialize an empty list to store the sorted elements
    merged_list = []
    
    # Extract the smallest element from the heap and add the next element from that list
    while min_heap:
        smallest, list_index = heapq.heappop(min_heap)
        merged_list.append(smallest)
        
        # Get the next element from the iterator of the list that had the smallest element
        next_element = next(iterators[list_index], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, list_index))
    
    return merged_list
