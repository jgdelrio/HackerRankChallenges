"""
CountDiv

Compute number of integers divisible by k in range [a..b].

Write a function:
    def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers
within the range [A..B] that are divisible by K, i.e.:
    { i : A <= i <= B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are 3 numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:
        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A <= B.
Complexity:
        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).
"""
import unittest
import random

MAX_INT = int(2e9)
INT_RANGE = (1, MAX_INT)


def solution(A, B, K):
    """
    :param A: start integer
    :param B: end integer
    :param K: divisor integer
    :return: count of integers A..B divisible by K
    """
    # As they set O(1), it just be a formula

    # Just depends whether A is part of the count itself, or not
    if A % K == 0:
        return B // K - A // K + 1
    else:
        return B // K - A // K
# The floor division tells as how many times is divisible
# in the top end (B//K) and in the lower end (A//K)


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution(6, 11, 2), 3)

    def test_small(self):
        self.assertEqual(solution(5, 11, 2), 3)
        self.assertEqual(solution(6, 12, 2), 4)
        self.assertEqual(solution(5, 12, 2), 4)
        self.assertEqual(solution(5, 13, 2), 4)

    def test_edges(self):
        self.assertEqual(solution(0, 0, 1), 1)
        self.assertEqual(solution(0, 1, 1), 2)
        self.assertEqual(solution(1, 1, 2), 0)
        self.assertEqual(solution(10, 20, 10), 2)
        self.assertEqual(solution(9, 21, 10), 2)

    def test_max_min(self):
        self.assertEqual(solution(0, MAX_INT, 1), MAX_INT + 1)


if __name__ == '__main__':
    unittest.main()
