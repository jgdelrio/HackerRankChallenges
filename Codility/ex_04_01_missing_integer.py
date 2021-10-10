"""
Missing Integer: Find the minimal positive integer not occurring in the given sequence.

Write a function:
    def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the minimal
positive integer (greater than 0) that does not occur in A.

For example, given:
  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.
Assume that:
    * N is an integer within the range [1..100,000]
    * each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
Complexity:
    * expected worst-case time complexity is O(N)
    * expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
        arguments).
Elements of input arrays can be modified.
"""

N_RANGE = (1, 100000)
ELEMENT_RANGE = (-2147483648, 2147483647)


def missing_integer(A):
    """
    :param A: non-empty list of integers
    :return: an integer - the smallest positive integer that is missing
    """
    # Initialize with the minimum positive integer known
    missing = 1
    # Go once through the array.
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            # Since is sorted I can stop once the element is bigger than the missing
            break
    return missing


def missing_integer_alternative_solution(A):
    """
    A 'Pidgeon Hole' solution:
    :param A: non-empty list of integers
    :return: an integer - the smallest positive integer that is missing
    """
    # dictionary of booleans indicating which ints we've seen
    roll = {}
    largest = 0

    # mark the roll
    for element in A:
        if element > 0:
            roll[element] = True
            # track the largest int
            if element > largest:
                largest = element

    # find the first missing element
    # NB: using `not in roll.keys()` contributes an O(N) loop which ruins time complexity on the codility platform
    counter = 1
    while counter <= largest:
        if counter in roll:
            counter += 1
        else:
            break

    return counter


TESTS = (
    ([2], 1),
    ([1], 2),
    ([-1], 1),
    ([1, 3, 6, 4, 1, 2], 5),
    ([2, 3, 4, 6, 10, 1000], 1),
    ([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000], 7),
    ([1000, -1, 10, 3, -5, 2, 11, 59, 1], 4),
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = missing_integer(input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
