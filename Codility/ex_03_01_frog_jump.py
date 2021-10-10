INT_RANGE = (1, 1000000000)


def frog_jump(X, Y, D):
    """
    Calculate the minimum number of jumps from X to Y
    :param X: start integer
    :param Y: minimum end integer
    :param D: size of the jump
    :return: minimum number of jumps in O(1) time and space complexity
    """
    # Sanity check: X is less than Y
    assert X <= Y

    # The trick for performance tests is do it in one single operation
    quot, rem = divmod(Y - X, D)
    return quot if rem == 0 else quot + 1


TESTS = (
    ((10, 85, 30), 3),
    ((0, 10, 1), 10),
    ((0, 10, 20), 1),
    ((10, 100, 10), 9),
    ((10, 10, 10), 0),
    ((9, 29, 10), 2),
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = frog_jump(*input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
