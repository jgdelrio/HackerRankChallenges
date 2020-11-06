"""
Practice > Algorithms > Strings > Weighted Uniform Strings

A weighted string is a string of lowercase English letters where each letter has a weight.
Character weights are  1  to  26  from  a  to  z  as shown below:

    a   1
    b   2
    ...
    y   25
    z   26

We define the following terms:
    - The weight of a string is the sum of the weights of all the string's characters. For example:
        apple = 1 + 16 + 16 + 12 + 5 = 50

    - A uniform string consists of a single character repeated zero or more times.
      For example, ccc and a are uniform strings, but bcb and cd are not.

Given a string, s, let U be the set of weights for all possible uniform contiguous substrings of string s.
You have to answer n queries, where each query i consists of a single integer, x[i].
For each query, print Yes on a new line if x[i] belongs to U; otherwise, print No instead.
"""
from time import time


TESTS = [
    (['abccddde', [1, 3, 12, 5, 9, 10]], ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']),
    (['aaabbbbcccddd', [9, 7, 8, 12, 5]], ['Yes', 'No', 'Yes', 'Yes', 'No']),
]


def letter2weight(letter):
    return ord(letter) - 96


def calculate_set(s):
    letter = s[0]
    count = 1
    weights = [letter2weight(letter)]
    for k in s[1:]:
        if k == letter:
            count += 1
            weights.append(count * letter2weight(letter))
        else:
            letter = k
            count = 1
            weights.append(letter2weight(letter))

    return set(weights)


def weightedUniformStrings(s, queries):
    """
    """
    result = []
    set_of_contiguous_substrings = calculate_set(s)

    for q in queries:
        if q in set_of_contiguous_substrings:
            result.append('Yes')
        else:
            result.append('No')
    return result


def hackerrank_run():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()


def test():
    data = TESTS

    for d in data:
        input = d[0]
        output = d[1]
        s, queries = input

        t0 = time()
        rst = weightedUniformStrings(s, queries)
        t1 = time() - t0
        print(f'Total time: {t1}')
        try:
            assert (rst == output)
        except AssertionError:
            print(f"Expected: {output}\t Received: {rst}")


if __name__ == '__main__':
    test()
