def find_Rotations_for_list(strings):
    def find_min_rotations(s):
        # Check if s is empty
        if not s:
            return 0
        
        # Create a new string that is the concatenation of the original string with itself
        doubled_s = s + s
        
        # Find the smallest index where the original string appears in this new doubled string
        # This effectively finds the rotation point where the string starts repeating
        for i in range(1, len(s) + 1):
            if s == doubled_s[i:i + len(s)]:
                return i
        return len(s)

    return [find_min_rotations(s) for s in strings]
