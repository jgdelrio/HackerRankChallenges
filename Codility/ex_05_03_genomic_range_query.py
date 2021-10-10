"""
GenomicRangeQuery

Find the minimal nucleotide from a range of sequence DNA

## Problem Description

https://codility.com/programmers/task/genomic_range_query/

A DNA sequence can be represented as a string consisting of the letters A, C, G and T,
which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer.
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.

You are going to answer several queries of the form:
What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of
nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T,
whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides,
in particular nucleotide A whose impact factor is 1, so the answer is 1.


Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q
consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.


# #### Analysis
If you're not fussy, this is a straightforward problem: you go through every query
and pull out the sliced sequence and  inspect it.  A quick sort to identify the least
impact nucleo and you're done. Right? See 'slow_solution' below. It scores about 65/100.

The straightforward solution visits every nucleotide in every slice. If the slices overlap a lot, then
the solution revisits the same nucleotide a lot.  If you could arrange the solution to
only visit each nucleotide once, then it would be much faster.

How?
We need to pass over the sequence and produce an intermediatory data structure which aggregates the data we
need into a directly accessible form; namely, without stepping through any part of the sequence again.

Enter the "prefix sum" pattern.
For this problem, we create an array for each type of item, then at each step through the sequence,
record the count of how many of each type we've seen.  When we're done, for the example sequence
 "CAGCCTA", we finish up with:
    sumA = [0,0,1,1,1,1,1,2]
    sumC = [0,1,1,1,2,3,3,3]
    sumG = [0,0,0,1,1,1,1,1]
    sumT = [0,0,0,0,0,0,1,1]

Now it's plain as day where each nucleo of each type appears.
So, when we can ask "Are there any 'C' types between points 2 and 4?"
we can lookup sumC for the answer:
  At point 2 we had seen 1 type C nucleo, and at point 4 we'd seen 2.  We determine
  there is exactly 1 (2-1) type C nucleo between points 2 and 4 only by looking at the two end-points,
  saving us from having to inspect every point between them.

So now we don't need the original sequence. Instead we can look at the sum for each endpoint
 and comparing the values.  Thus we can quickly identify which nucleotides appear in each query
 and determine the 'minimum impact' value within each.

See 'fast_solution'. Scores 100/100.
"""
import unittest
import random

# maximum number of neucleotides in a sequence
MAX_N = 100000
# maximum number of queries
MAX_M = 50000

# impact factor of each neucleotide
M = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


def slow_solution(S, P, Q):
    """
    An easy to implement and understand solution: O(N * M)
    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    https://codility.com/demo/results/trainingC9QT9A-BQS/
    """
    # for every query, sort the sequence slice into alphabetical order: the first char will be the minimal-factor
    result = []
    for p, q in zip(P, Q):
        slice = sorted(S[p:q + 1])
        # As it is sorted we only look at [0] to pick the smallest factor
        result.append(M[slice[0]])
    return result


def fast_solution(S, P, Q):
    """
    A faster, but more difficult to implement and understand, solution: 0(N + M)
    :param S: a string of 1..MAX_N chars containing a mix of the four chars A, C, G, and T
    :param P: a list of integers indexing a position in S
    :param Q: a list of integers indexing a position in S
    :return: a list of ints between 1 and 4, one for each query
    https://codility.com/demo/results/trainingH6PA4P-5V7/
    """
    # Pass 1: Create suffix sums
    # We build four lists, one for each nucleo, which are as long as the sequence itself (plus one).
    # The lists preserve the sequence order and track the sum total of how many times we've seen that
    # nucleo type as we progress through the list.
    sumA = [0]
    sumC = [0]
    sumG = [0]
    sumT = [0]

    for nucleo in S:
        # copy the counts in the last cell into this one
        for sum in (sumA, sumC, sumG, sumT):
            sum.append(sum[-1])
        # increment the sum corresponding to the current nuke
        if nucleo == 'A':
            sumA[-1] += 1
        elif nucleo == 'C':
            sumC[-1] += 1
        elif nucleo == 'G':
            sumG[-1] += 1
        else:
            sumT[-1] += 1

    # Pass 2: Evaluate the queries
    # Each query defines a slice via indicies P and Q which correspond to the start and end points.
    # By comparing the sum at both points we can readily determine how many nucleos of that type
    # appear within them.
    # Eg: In the sum [0,1,1,1,2,3,3,3], at index 2 there is a 1, and at index 4, there is a 2.
    # Thus, somewhere between indexes 2 and 4, there must have been a nucleo of type 'C'.
    # Additionally, we can determine how many 'C' nucleos are there by subtracting one sum from the other (2-1=1).
    impact = []
    for p, q in zip(P, Q):
        # Check 1st the smallest options
        if sumA[q + 1] > sumA[p]:
            impact.append(M['A'])
        elif sumC[q + 1] > sumC[p]:
            impact.append(M['C'])
        elif sumG[q + 1] > sumG[p]:
            impact.append(M['G'])
        else:
            impact.append(M['T'])
    return impact


solution = fast_solution


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]), [2, 4, 1])

    def test_random(self):
        seq = [random.choice("ACGT") for _ in range(1, 5000)]
        P_array, Q_array = [], []
        for _ in range(0, len(seq)):
            P = random.randint(0, len(seq) - 1)
            Q = random.randint(P, len(seq) - 1)
            P_array.append(P)
            Q_array.append(Q)
        solution(seq, P_array, Q_array)

    def test_extreme(self):
        S = 'T' * MAX_N
        P = [0] * MAX_M
        Q = [MAX_N - 1] * MAX_M
        self.assertEqual(solution(S, P, Q), [4] * MAX_M)


if __name__ == '__main__':
    unittest.main()
