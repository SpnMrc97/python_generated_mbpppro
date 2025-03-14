def is_sequence_of_sublists(list_of_lists, sequence_of_sublists):
    if not sequence_of_sublists:  # An empty sequence is trivially found
        return True
    
    len_main = len(list_of_lists)
    len_seq = len(sequence_of_sublists)

    # Iterate through the main list to find the start of the sequence
    for i in range(len_main - len_seq + 1):
        # Check if the sublist from i to i + len_seq matches the sequence
        if list_of_lists[i:i + len_seq] == sequence_of_sublists:
            return True

    return False
