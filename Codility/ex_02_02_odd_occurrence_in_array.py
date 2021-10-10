import random

# the largest length array we have to handle
MAX_LENGTH = 1000000


def odd_occurrence(A):
    """
    Find the value that does not have a match in an odd sized array
    :param A: an array of integers with an odd number of elements
    :param N: length of the array
    :return: the one element which does not have a complementary element
    """
    # Sanity checks
    if not isinstance(A, list):
        raise TypeError("Input must be a list of integers")
    if len(A) < 1:
        raise ValueError("Input list must not be empty")
    if len(A) > MAX_LENGTH:
        raise ValueError("Input list must not be longer than %s" % MAX_LENGTH)

    # dictionary holder for keys in need of a match
    unmatched = dict()

    # Loop every element once
    for element in A:
        # Try removing it's match. If not exists, the exception will add it to the unmatched
        try:
            del unmatched[element]
        except KeyError:
            # else add it
            unmatched[element] = True

    if len(unmatched) == 1:
        # Single unmatched element
        return next(iter(unmatched.keys()))
    else:
        raise Exception("Expected one unmatched item, but have this: %s" % unmatched)


def gen_array(length, odd):
    """generate a list of sample data: random integers in pairs
    :param L: the length of the list is double this int
    :param odd: the odd integer out
    """
    arr = []
    for _ in range(int((length - 1) / 2)):
        val = random.randint(1, MAX_LENGTH)
        arr.extend((val, val))
    arr.append(odd)
    random.shuffle(arr)
    return arr


TESTS = (
    ([42], 42),
    ([9, 3, 9, 3, 9, 7, 9], 7),
    (gen_array(5, 4), 4),
    (gen_array(11, 4), 4),
    (gen_array(601, 4242), 4242),
    (gen_array(999999, 5000111222), 5000111222)
)


def run_tests():
    for test in TESTS:
        input = test[0]
        expected = test[1]
        result = odd_occurrence(input)

        assert result == expected


if __name__ == '__main__':
    run_tests()
