
def solution(A, K):
    """
    Rotate/shift the array A by k steps
    :param A: an array of integers
    :param K: number of times to shift right
    :return: the rotated array
    """
    # A is empty
    if not len(A):
        return A

    # netK is the net number of shifts to apply (omits spinning round and round)
    netK = (len(A) + K) % len(A)
    if netK > 0:
        head = A[len(A) -netK:]
        tail = A[:-netK]
        return head + tail
    else:
        return A
