def is_consistent_patterns(colors_list, patterns_list):
    if len(colors_list) != len(patterns_list):
        return False
    
    # To store the mapping of pattern to color
    pattern_to_color = {}
    
    for colors, patterns in zip(colors_list, patterns_list):
        if len(colors) != len(patterns):
            return False
        
        # Temporary mapping for the current list
        current_mapping = {}
        
        for color, pattern in zip(colors, patterns):
            if pattern in pattern_to_color:
                if pattern_to_color[pattern] != color:
                    return False
            else:
                current_mapping[pattern] = color
        
        # Verify if the current mapping is consistent with the global mapping
        for pattern, color in current_mapping.items():
            if pattern in pattern_to_color:
                if pattern_to_color[pattern] != color:
                    return False
            else:
                pattern_to_color[pattern] = color
    
    # Ensure each pattern maps to a unique color
    if len(set(pattern_to_color.values())) != len(pattern_to_color):
        return False
    
    return True
