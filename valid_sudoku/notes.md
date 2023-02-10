[Medium]
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

---
The hard part here seems like figuring out how to dissect a 2d array. Actually, now that I think about it...... my original thought was to look at the each row and each column and check for duplicates and then do the same with each 3x3 box, but I think a BFS could be applicable here. The way it would work is starting from the top left corner, and at each point, it would check if the number chosen in the actual puzzle was valid and then expand out to the rest of its neighbors.  It returns true if all its neighbors are valid and false otherwise. Hmm, just realized that will create some complications with how to handle the quadrants. Need to think that through more. Going back to my original thought about just checking rows and columns against duplicates.

After 45 min: here's the solution i came up with.

```
```python
def has_duplicates(arr):
        filtered_list = list(filter(lambda x: x != ".", arr))
        unique_values = set(filtered_list)
        return len(filtered_list) != len(unique_values)
  
      def is_valid_sudoku(puzzle):
          # check horizontal
          for lst in puzzle:
              if has_duplicates(lst):
                  return False
      
          # check vertical
          vertical_lists = [[x[y] for x in puzzle] for y in range(len(puzzle))]
      
          for lst in vertical_lists:
              if has_duplicates(lst):
                  return False
      
          # check sub boxes
          for sub_box in range(9):
              section = (sub_box // 3) * 3
              group = sub_box % 3
              start = group * 3
     
              first_three = puzzle[section][start : start + 3]
              second_three = puzzle[section + 1][start: start + 3]
              last_three = puzzle[section + 2][start: start + 3]
      
              if has_duplicates(first_three + second_three + last_three):
                  return False
      
          return True
```

Beats 75% on runtime.
