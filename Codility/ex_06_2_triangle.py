"""
Triangle

Determine whether a triangle can be built from a given set of edges.
https://codility.com/programmers/task/triangle/


# Problem Description

A zero indexed array A consisting of N integers is given.
A triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:
        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:
    def solution(A)
that, given a zero-indexed array A consisting of N integers,
returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Assume that:
        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
Complexity:
        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage
        (not counting the storage required for input arguments).
Elements of input arrays can be modified.

----------------
# Analysis
The obvious solution is indeed that and pretty quick to come to, but scores only 75% (100, 33),
as it has to run through all the combinations: O(N**3)

The fast solution uses the not-so-obvious observation that testing the three numbers closest
together is your best <cough-certain> chance of identifying a 'triangle'.
Thus providing for a sort (O(log(N) and a single pass O(N)) => O(N * log(N))

eg:
input: [10, 2, 5, 1, 8, 20]
sorted: [1, 2, 5, 8, 10, 20]

tests:
[1,2,5] = 3 > 5 = 0
[2,5,8] = 7 > 8 = 0
[5,8,10] = 13 > 10 = 1!

eg:
input: [10, 50, 5, 1]
sorted: [1, 5, 10, 50]

tests:
[1,5,10] = 6 > 10 = 0
[5,10,50] = 15 > 50 = 0
"""

import unittest
import random

import itertools

RANGE_A = (-2147483648, 2147483647)
RANGE_N = (0, 100000)


def obvious_solution(A):
    """
    100% correct but only 33% performant = 75% score
    :param A: array of integers
    :return: an integer
    """

    def is_triangle(P, Q, R):
        """true when P, Q, and R form a 'triangle'"""
        return (P + Q > R) and (Q + R > P) and (R + P > Q)

    result = 0
    # do a factorial visit of every combination
    for P, Q, R in itertools.combinations(A, 3):
        if is_triangle(P, Q, R):
            # print A, P, Q, R
            result = 1

    return result


def fast_solution(A):
    """
    :param A: array of integers
    :return: 1 if there is a triangle, otherwise 0
    """

    def is_triangle(P, Q, R):
        """true when P, Q, and R form a 'triangle'"""
        return (P + Q > R) and (Q + R > P) and (R + P > Q)

    A.sort()

    # Only evaluates the three closest numbers together
    # as is the best chance of hitting a triangle
    for i in range(len(A) - 2):
        if is_triangle(A[i], A[i + 1], A[i + 2]):
            return 1
    return 0


solution = fast_solution


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)
        self.assertEqual(solution([10, 50, 5, 1]), 0)

    def test_lowballs(self):
        self.assertEqual(0, solution([]))
        self.assertEqual(0, solution([0]))
        self.assertEqual(0, solution([0, 1]))

    def test_simple(self):
        A = [5, 3, 3]
        self.assertEqual(1, solution(A))

    def test_large_negative(self):
        self.assertEqual(0, solution([-1] * RANGE_N[1]))


if __name__ == '__main__':
    unittest.main()
