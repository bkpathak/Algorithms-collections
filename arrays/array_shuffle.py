# Shuffle-Yates-Knuth Implementation
# This is the simple problem but is prone to incorrect implementation and bias result instead of uniform distribution.

# Simple implementation with bias result

import random
import unittest
from collections import defaultdict

def bias_shuffle(in_list):
    for i in range(len(in_list)):
        random_index = random.randint(0, len(in_list) - 1)
        # swap items
        in_list[i], in_list[random_index] = in_list[random_index], in_list[i]
    return in_list

# Why biased?
# If list has 3 element; each position has 3 possible outcomes which leads to total outcomes of 3^3 = 27.
# But from theory the number of possible outcomes of 3 items is 3 * 2 * 1, which is 3!(N!). So the above algorithm will
# be biased algorithm since 27 % 6 != 0.


def uniform_shuffle(in_list):
    for i in range(len(in_list)):
        random_index = random.randint(i, len(in_list) - 1)
        # swap items
        in_list[i], in_list[random_index] = in_list[random_index], in_list[i]

    return in_list

# Why uniform?
# The above two algorithm has slight difference how we pick up the random_index. In bias the random_index is always
# between(inclusive) 0 - N -1 , where as in uniform the range shrinks in every loop, initially it's in the range of
# 0 - N - 1 , and 0 - N-2, 0 - N-3 ... . So from theory we know we have N items has N! possible outcomes, N * N - 1 *
# N-2 * ... N-N.

class ShuffleTest(unittest.TestCase):
    def test_bias_shuffle(self):
        shuffle_count = {}
        for i in range(6000):

if __name__ == "__main__":