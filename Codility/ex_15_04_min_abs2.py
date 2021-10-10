"""
Let A be a non-empty zero-indexed array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:
  A[0] =  1
  A[1] =  4
  A[2] = -3

has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
    The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
    The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
    The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
    The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
    The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
    The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.


Write a function:
    def solution(A)
that, given a non-empty zero-indexed array A consisting of N integers,
returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:
  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:
  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.


Assume that:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

Complexity:
- expected worst-case time complexity is O(N*log(N));
- expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""
import unittest


def solution(A):
    """
    As in the example, the best chance of the smaller result is to combine a positive and a negative value
    For that, we sort the array and then we move starting from the front and the back
    moving to the inside of the array
    """
    N = len(A)

    if N == 1:
        return abs(A[0] * 2)

    A.sort()

    ini = 0
    end = N - 1
    min_sum = abs(A[ini] + A[end])

    while ini < end:
        # Allocate the new possible locations and measure what happens...
        new_ini = ini + 1
        new_end = end - 1

        # New abs sum if we shift the ini to the right
        new_val_front = abs(A[new_ini] + A[end])

        # New abs sum if we shift the end to the left
        new_val_back = abs(A[ini] + A[new_end])

        if new_val_front < new_val_back:
            # Shifting front ptr is better
            min_sum = min(new_val_front, min_sum)
            ini = new_ini
        else:
            # Shifting back ptr is better
            min_sum = min(new_val_back, min_sum)
            end = new_end

    return min_sum


class TestExercise(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([1, 4, -3]), 1)

    def test_example2(self):
        self.assertEqual(solution([-8, 4, 5, -10, 3]), 3)

    def test_single_element(self):
        self.assertEqual(solution([2]), 4)

    # def test_zero_case(self):
    #     self.assertEqual(solution([-8, 4, 5, -10, 3]), 3)


if __name__ == '__main__':
    unittest.main()
