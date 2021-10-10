import pytest
from hamcrest import assert_that, equal_to

# The largest integer we have to deal with
MAXINT = 2147483647


def binary_gap(n):
    """
    Determines the maximal 'binary gap' in an integer
    :param n: a positive integer (between 1 and maxint or 2million odd)
    :return: a count of the longest sequence of zeros in the binary representation of the integer
    """
    # Sanity checks
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")

    # convert the number to a string containing '0' and '1' chars
    binary_string = str(bin(n))[2:]

    # the longest binary gap: use None to indicate no 'gap' yet found (set to zero at the first flip)
    max_count = None
    # count the bits in the sequence
    this_count = 0
    # true if the last bit was a zero
    was_zero = None

    # loop over all the 0/1 chars in the string
    for bit in binary_string:
        is_zero = bit == '0'

        # if the bit value has flipped
        if bool(was_zero) != bool(is_zero):
            # the first sequence doesn't count eg: 1111001 has a result of 2
            if max_count is None:
                max_count = 0
            # save the biggest gap
            elif this_count > max_count:
                max_count = this_count
            # reset the counter
            this_count = 1
        else:
            # increment the length of the sequence
            this_count += 1

        # track what the last bit was
        was_zero = is_zero

    # print "%s: %s = %s" % (N, binary_string, max_count)
    if max_count is not None:
        return max_count
    else:
        # no binary gaps found
        return 0


TESTS = (
    (1041, 5),
    (15, 0),
    (1, 0),
    (5, 1),
    (9, 2),
    (51712, 2),
    (1610612737, 28),
)


@pytest.mark.parametrize('input, expected', TESTS)
def test_binary_gap(input, expected):
    rst = binary_gap(input)
    print(f"Input: {input} \tResult: {expected}")
    assert_that(rst, equal_to(expected))


if __name__ == '__main__':
    test_binary_gap()
