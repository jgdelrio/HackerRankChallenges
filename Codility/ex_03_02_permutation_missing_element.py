"""
Find the missing element in a list which is a permutation of elements.

The assumptions are:
- The minimum permutation is 2 numbers
- The permutations are 1...len(A)
"""

def missing_element(A):
    """
    Find the missing element in a given permutation
    :param A: list of integers
    :return: the integer that is missing in O(n) time and O(1) space complexity
    """
    # An empty list so the missing element must be "1"
    if len(A) == 0:
        return 1
    # Add all expected elements and subtract the sum of the ones in the list
    # The list should start from 1, and range goes to len - 1, so we add 2
    return sum(range(1, len(A) + 2)) - sum(A)


TESTS = (
    ([1], 2),
    ([2], 1),
    ([2, 3, 1, 5], 4),
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = missing_element(input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
