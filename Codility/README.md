# [Codility](https://codility.com)

Solutions to the [exercises and tests](https://app.codility.com/programmers/lessons/) 

## Test cases

Their test cases follow a predictable methodology :

* Examples provided are explicitly tested

#### Correctness tests
* Empty or zero test case: the expected result is often not explicit or obvious, but will actually be there implicitly, such that you may not realise it is indeed specified until you work out what the answer should be.
* Minimal test case: using just one input, or whatever is the absolute minimal conceivable input - again, probably not explicitly described, but there implicitly nonetheless
* Edge cases: cases written to root out those awkward -off-by-one- scenarios that inevitably suck up 80% of the time required to devise a solution
* Simple tests: just some basic, as you might reasonably anticipate, examples

#### Performance tests

* Worst case scenario: the biggest possible numbers in the biggest resultsets - with the intent to test the speed and space restraints
* Medium sized tests: not always, as the problem dictates (ex: ~100 - ~5000 length arrays)
* Extreme Case: always, typically involving generating maximal random datasets

## Other notes

* you're safe to assume they won't test, mark you down for, failing to guard against the explicit assumptions described. So if it says N is 0..1000, they won't feed in an N=1001 just to see if you protected against it.
* the "Open reading material", currently at the top of each lesson, is worth reading before attempting the exercises as they are short and focus exactly on what you'll need to solve the following puzzles
* during the actual interview testing/exam, the report sent to the candidate is much more sparesly detailed than the one sent to the company?!
* if you use the browser to actually build your solution - every edit and run is recorded and presented to the client
* if you are given multiple tasks, you are permitted to read them, and commence them, and submit them in any order.
* if there seems to be a lack of specificity in every puzzle around what is the correct response to error conditions; look, read, look again, as
   after seeing the solution that apparent lack always seems like a debateably reasonable assumption implied by the specs.
   For example:
    * "MissingInteger" (Lesson 4) does not specify the correct response if the input sequence is [-1,-2,-3]:
   there are no positive integers so what is the correct response? The 'minimal positive integer' is 1.
    * Similarly, it does not explicitly state that if the input set is _full_ (no integers are missing) then return 
   the largest value—plus one.  Again, seems perfectly reasonable in hindsight, but a source of uncertainty in the moment
* before submitting your solution, there is no feedback regarding it's efficiency; but it does affect your score and report
* Understanding the O factors reveals the nature of the optimal solution:
   * O(1) there is a formulaic solution 
   * O(n) the solution has no nested loops and all happens in a single pass
   * O(n+m) the solution has no nested loops, and passes over n and m only once
   * O(n+n) the solution has no nested loops, but you can pass over the sequence twice
   * O(n*n) the solution has a loop through n nested inside a loop through n
* the python `in` operator is a list loop and could contribute an O(N) all on it's own. ie:
    * `foo in bar` is ok if bar is a dictionary, but a potential problem if bar is a list
    * `foo in bar.keys()` is a nested loop (sequentially visiting every item in the list of keys)
* coming up with reasonable test cases, and determining the correct answers, is half the puzzle! Passing the example
   is not enough. Every puzzle is subjected to 'simple' tests, not unlike the one provided, and 'medium' tests-
   which involve arrays of significant length, to be sure you pass these tests you need to work out some way
   to generate a sizeable test sequence but still know the correct answer. Then there are the 'maximal' tests which
   seek to max-out the size and complexity so, to be certain of 100%, you need to devise tests-and the correct
    answers-for that too.
