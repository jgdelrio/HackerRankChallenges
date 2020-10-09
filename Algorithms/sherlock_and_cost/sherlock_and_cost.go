package main

import (
	"fmt"
)

func main() {
	B := []int{1, 3, 3}
	fmt.Println("Calculated cost for ", B, " is ", Cost(B))
}

// makeRange creates a sequence from min to max(with max excluded)
func makeRange(min, max int) []int {
	a := make([]int, max-min)
	for i := range a {
		a[i] = min + i
	}
	return a
}

// Max calculates the max for type int
func Max(val0, val1 int) int {
	if val0 > val1 {
		return val0
	}
	return val1
}

// Abs calculates the Abs for type int
func Abs(val int) int {
	if val >= 0 {
		return val
	}
	return -val
}

// Cost calculates the max Cost of the optimal A matrix to solve Sherlock And Cost
func Cost(B []int) int {
	// Initialization
	var hi, low int = 0, 0
	var n = len(B)

	for _, i := range makeRange(1, n) {
		highToLowDiff := Abs(B[i-1] - 1)     // Value if we finish at 'i' low (1)
		lowToHighDiff := Abs(B[i] - 1)       // Value if we finish at 'i' high (B[i])
		highToHighDiff := Abs(B[i] - B[i-1]) // Diff between current B[i] and previous

		nextLow := Max(low, hi+highToLowDiff)               // accum in low
		nextHi := Max(hi+highToHighDiff, low+lowToHighDiff) // accum in high

		low = nextLow
		hi = nextHi
	}
	return Max(hi, low)
}

// Practice > Algorithms > Dynamic Programming > Sherlock and Cost

// In this challenge, you will be given an array B and must determine an array A.
// There is a special rule: For all i, A[i] <= B[i].
// That is, A[i] can be any number you choose such that 1<= A[i] <= B[i].
// Your task is to select a series of A[i] given B[i] such that the sum of the absolute difference
// of consecutive pairs of A is maximized. This will be the array's cost,
// and will be represented by the variable S below.

// The equation can be written:

//         S = SUM(i=2toN)  |A[i] - A[i-1]|

// For example if B = [1,2,3]
// The possible A arrays are:
//     [1,1,1], [1,1,2], [1,1,3]
//     [1,2,1], [1,2,2], [1,2,3]

// Our calculations for the arrays are as follows:
//     |1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
//     |2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2

// The maximum value obtained is 2
