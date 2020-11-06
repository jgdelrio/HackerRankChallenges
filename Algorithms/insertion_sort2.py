"""
Practice > Algorithms > Sorting > Insertion Sort - Part 2

In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position.
Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array.
How can you use that code to build up a sorted array, one element at a time?
Note that in the first step, when you consider an array with just the first
element, it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort,
i.e., whenever the next element has been inserted at its correct position.
Since the array composed of just the first element is already sorted,
begin printing after placing the second element.

For example, there are  n=7  elements in  arr = [3,4,7,5,6,2,1].
Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7

Input
-----
 - n: an integer representing the length of the array  arr
 - arr: an array of integers

"""
from time import time


TESTS = [([1, 4, 3, 5, 6, 2], [ [1, 4, 3, 5, 6, 2],
                                [1, 3, 4, 5, 6, 2],
                                [1, 3, 4, 5, 6, 2],
                                [1, 3, 4, 5, 6, 2],
                                [1, 2, 3, 4, 5, 6] ]),
        ([8, 7, 6, 5, 4, 3, 2, 1], [ [7, 8, 6, 5, 4, 3, 2, 1],
                                     [6, 7, 8, 5, 4, 3, 2, 1],
                                     [5, 6, 7, 8, 4, 3, 2, 1],
                                     [4, 5, 6, 7, 8, 3, 2, 1],
                                     [3, 4, 5, 6, 7, 8, 2, 1],
                                     [2, 3, 4, 5, 6, 7, 8, 1],
                                     [1, 2, 3, 4, 5, 6, 7, 8] ]),
]


def find_pos(idx, arr):
    final_pos = None
    for pos in range(idx-1, -1, -1):
        if arr[idx] < arr[pos]:
            final_pos = pos
    return final_pos


def insertionSort2(n, arr):
    """
    Starting at index idx, lift the value from 1 and then
    keep going backwards until the discovery of the correct position
    then shuffle the array (the the position to idx)
    then shove the value from idx
    continue from idx
    """
    result = []
    for idx, val in enumerate(arr[1:]):
        idx = idx + 1
        new_pos = find_pos(idx, arr)
        if new_pos is not None:
            val = arr.pop(idx)
            arr = [*arr[:new_pos], val, *arr[new_pos:]]
        result.append(arr.copy())
        # Update to:   print(' '.join(map(str, arr.copy())))    in hackerRank

    return result


def hackerrank_run():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)


def test():
    data = TESTS

    for d in data:
        input = d[0]
        output = d[1]
        n = len(input)

        t0 = time()
        rst = insertionSort2(n, input)
        t1 = time() - t0
        for k in rst:
            print(k)
        print(f'Total time: {t1}')
        assert (rst == output)


if __name__ == '__main__':
    test()
