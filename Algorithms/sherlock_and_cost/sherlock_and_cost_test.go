package main

import "testing"

var testList = []testCase{
	testCase{caseData: []int{10, 1, 10, 1, 10}, expected: 36},
	testCase{caseData: []int{2, 4, 3}, expected: 6},
	testCase{caseData: []int{100, 2, 100, 2, 100}, expected: 396},
}

type testCase struct {
	caseData []int // input
	expected int   // expected result
}

func TestCost(t *testing.T) {
	for _, tc := range testList {
		give := tc.caseData
		want := tc.expected
		if got := Cost(give); got != want {
			t.Errorf("Cost() = %d, want %d", got, want)
		}
	}
}
