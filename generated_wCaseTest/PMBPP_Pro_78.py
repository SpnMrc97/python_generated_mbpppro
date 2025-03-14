def sum_tuples_to_int(tuples_list):
    """
    Convert each tuple of positive integers into a single integer by treating the elements as digits,
    and sum all these integers together.

    Parameters:
    tuples_list (list of tuples): A list where each element is a tuple of positive integers.

    Returns:
    int: The sum of all integers formed from the tuples.
    """
    total_sum = 0

    for tpl in tuples_list:
        # Convert the tuple into a single integer
        number_str = ''.join(map(str, tpl))
        number = int(number_str)
        # Add the integer to the total sum
        total_sum += number

    return total_sum

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sum_tuples_to_int([(1, 2), (3, 4)]) == 46
assert sum_tuples_to_int([(1,), (2, 3), (4, 5, 6)]) == 1 + 23 + 456
assert sum_tuples_to_int([]) == 0
assert sum_tuples_to_int([(9, 9, 9), (1, 0, 0)]) == 999 + 100
assert sum_tuples_to_int([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == 123 + 456 + 789

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)