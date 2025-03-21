import re

def filter_lowercase_underscore_strings(strings):
    # Define a regular expression pattern that matches only lowercase letters joined by underscores
    pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    
    # Use a list comprehension to filter strings that match the pattern
    filtered_strings = [s for s in strings if pattern.match(s)]
    
    return filtered_strings
