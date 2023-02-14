**Q:** You are implementing an aggregation function. Your aggregator will accept input from this function call `Process([]int)`, expect it to be called multiple times. 
Focus on correctness over time and space efficiency. Feel free to use any built-in data structure.

**Input**
- array of unordered integers (eg [5,3,6,1])

**Output**
- sub-arrays of at least two consecutive, ordered integers
- integers that are not a part of a consecutive array must be remembered for subsequent `Process` calls,
Example: Call `Process` 5 times
Process([]) -> []
Process([7,6]) -> [6,7]
Process([5,3,8,9,1,4]) -> [3,4,5],[8,9] // 1 is ignored
Process([2]) -> [1,2]  // notice that 1 was stored from the previous call
Process([7,6]) -> [6,7]
Process([2,3]) -> [2,3] // notice that 1 is no longer available to be used again