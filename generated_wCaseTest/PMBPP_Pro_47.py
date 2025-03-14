def medians_of_triplets(lst):
    """
    This function takes a list of integers and returns a list containing the median of each triplet.
    If the list length is not a multiple of three, the remaining elements are ignored.
    
    :param lst: List of integers
    :return: List of medians of each triplet
    """
    medians = []
    # Process the list in chunks of three
    for i in range(0, len(lst) - len(lst) % 3, 3):
        triplet = lst[i:i+3]
        triplet.sort()  # Sort the triplet
        median = triplet[1]  # The second element is the median after sorting
        medians.append(median)
    return medians

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert medians_of_triplets([1, 2, 3, 4, 5, 6]) == [2, 5]
assert medians_of_triplets([10, 20, 30, 40, 50, 60, 70]) == [20, 50]
assert medians_of_triplets([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert medians_of_triplets([5, 3, 8, 9, 1, 7, 4, 6, 2]) == [5, 7, 4]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)