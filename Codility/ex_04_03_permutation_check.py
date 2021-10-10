"""
PermCheck
Check whether array A is a permutation.
A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
    int solution(int A[], int N);
that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
Assume that:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
Complexity:
        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

ARR_RANGE = (1, 100000)
INT_RANGE = (1, 1000000000)


def is_permutation(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # An empty list is not a permutation
    if not len(A):
        return 0

    # track the hits with a dictionary
    hits = {}
    for item in A:
        # (quick exit) each element once and only once
        if item in hits:
            # Duplicated elements
            return 0
        hits[item] = True

    # check if they're all there
    for num in range(1, len(A) + 1):
        if num not in hits:
            return 0

    return 1


def is_permutation_alternative(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # An empty list is not a permutation
    if not len(A):
        return 0

    # track the hits with a dictionary
    hits = {}
    for item in A:
        # (quick exit) each element once and only once
        if item in hits:
            # Duplicated elements
            return 0
        hits[item] = True

    # Alternative solution
    # If there are missing values, the max value and the length are going to differ
    max_val = max(A)
    if (max_val > len(A)) or (max_val > len(hits)):
        return 0

    return 1


TESTS = (
    ([], 0),
    ([1], 1),
    ([2], 0),
    ([1, 2, 3], 1),
    ([5, 2, 1], 0),
    ([4, 1, 3, 2], 1),
    ([4, 1, 3], 0),
    ([3, 3, 3, 3, 2, 1], 0),
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = is_permutation(input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
