N_RANGE = (2, 100000)
ELEMENT_RANGE = (-1000, 1000)


def tape_equilibrium(A):
    """
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
    :param A: non-empty list of integers
    :return: an integer - the index value where the smallest difference occurs
    """
    # Sanity check
    assert len(A) > 1

    # Establish the tallys
    best = None
    before = 0
    after = sum(A)

    # Adjust and test at every split. Loop once.
    for P in range(0, len(A) - 1):
        before += A[P]
        after -= A[P]
        difference = abs(before - after)
        if best is None or difference < best:
            best = difference
    return best


TESTS = (
    ([1, 2], 1),
    ([3, 1, 2, 4, 3], 1),
    ([-1000, 1000], 2000),
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = tape_equilibrium(input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
