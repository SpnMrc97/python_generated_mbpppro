from collections import defaultdict

def flatten(nested_list):
    """Flatten a nested list of arbitrary depth."""
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element

def frequency_nested_lists(nested_list):
    """Calculate the frequency of each element in a nested list."""
    frequency_dict = defaultdict(int)
    
    for element in flatten(nested_list):
        frequency_dict[element] += 1
        
    return dict(frequency_dict)
