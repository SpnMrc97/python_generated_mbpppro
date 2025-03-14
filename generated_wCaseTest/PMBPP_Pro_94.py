def smallest_power_of_2_for_sum(lst):
    if not lst:
        return 0

    total_sum = sum(lst)
    power_of_2 = 1

    while power_of_2 < total_sum:
        power_of_2 *= 2

    return power_of_2

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert smallest_power_of_2_for_sum([1, 2, 3]) == 8
assert smallest_power_of_2_for_sum([5, 5, 5]) == 16
assert smallest_power_of_2_for_sum([]) == 0
assert smallest_power_of_2_for_sum([16, 16, 16]) == 64
assert smallest_power_of_2_for_sum([1, 1, 1, 1, 1, 1, 1, 1]) == 8

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)