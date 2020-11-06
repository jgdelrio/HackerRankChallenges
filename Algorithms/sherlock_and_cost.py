"""
Practice > Algorithms > Dynamic Programming > Sherlock and Cost

In this challenge, you will be given an array B and must determine an array A.
There is a special rule: For all i, A[i] <= B[i].
That is, A[i] can be any number you choose such that 1<= A[i] <= B[i].
Your task is to select a series of A[i] given B[i] such that the sum of the absolute difference
of consecutive pairs of A is maximized. This will be the array's cost,
and will be represented by the variable S below.

The equation can be written:

        S = SUM(i=2toN)  |A[i] - A[i-1]|

For example if B = [1,2,3]
The possible A arrays are:
    [1,1,1], [1,1,2], [1,1,3]
    [1,2,1], [1,2,2], [1,2,3]

Our calculations for the arrays are as follows:
    |1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
    |2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2

The maximum value obtained is 2

"""

import os
from time import time


TESTS = [
    [(10, 1, 10, 1, 10), 36],
    [(2, 4, 3), 6],
    [(100, 2, 100, 2, 100), 396]
]


def cost(B: list) -> int:
    # Initialization
    hi, low, n = 0, 0, len(B)

    # Skip 0
    for i in range(1, n):
        high_to_low_diff = abs(B[i - 1] - 1)        # Value if we finish at 'i' low (1)
        low_to_high_diff = abs(B[i] - 1)            # Value if we finish at 'i' high (B[i])
        high_to_high_diff = abs(B[i] - B[i - 1])    # Diff between current B[i] and previous

        next_low = max(low, hi + high_to_low_diff)                      # accum in low
        next_hi = max(hi + high_to_high_diff, low + low_to_high_diff)   # accum in high

        low = next_low
        hi = next_hi

    return max(hi, low)


def hackerrank_run():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        B = list(map(int, input().rstrip().split()))
        result = cost(B)
        fptr.write(str(result) + '\n')

    fptr.close()


def test():
    data = TESTS
    for d in data:
        input = d[0]
        output = d[1]

        t0 = time()
        rst = cost(input)
        t1 = time() - t0
        if not rst == output:
            print(f"{input} Expected: {output} Result: {rst}")
        print(f'Total time: {t1}')


if __name__ == '__main__':
    test()
