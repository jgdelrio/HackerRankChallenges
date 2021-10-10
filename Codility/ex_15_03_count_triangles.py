"""
A zero-indexed array A consisting of N integers is given.
A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R].
In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
    A[P] + A[Q] > A[R],
    A[Q] + A[R] > A[P],
    A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array,
namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).


Write a function:   def solution(A)
that, given a zero-indexed array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.


Assume that:
- N is an integer within the range [0..1,000];
- each element of array A is an integer within the range [1..1,000,000,000].

Complexity:
- expected worst-case time complexity is O(N2);
- expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""
import unittest


def solution(A):
    """
    There are a couple of cases to realise.
    - We need at least 3 numbers, otherwise we have 0 triangles
    - Sorting the array allows us to compare the closest numbers with the conditions of the triangle
    """
    N = len(A)

    if N < 3:
        # Less than 3 sides so no triangles can be made
        return 0

    A.sort()
    triangles_count = 0

    for left in range(0, N - 2):
        right = left + 2

        for mid in range(left + 1, N - 1):
            while right < N and A[left] + A[mid] > A[right]:
                # The array is sorted, so the number of mid sides between mid and right is valid.
                triangles_count += right - mid
                right += 1

    return triangles_count


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 12]), 4)

    def test_zero_case(self):
        self.assertEqual(solution([1, 2]), 0)

    def test_min_case(self):
        self.assertEqual(solution([3, 4, 5]), 1)


if __name__ == '__main__':
    unittest.main()
