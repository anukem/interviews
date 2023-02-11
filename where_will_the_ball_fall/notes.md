[Medium]
You have a 2-D `grid` of size `m x n` representing a box, and you have `n` balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

-   A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as `1`.
-   A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as `-1`.

We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return _an array_ `answer` _of size_ `n` _where_ `answer[i]` _is the column that the ball falls out of at the bottom after dropping the ball from the_ `ith` _column at the top, or `-1` _if the ball gets stuck in the box_._

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/09/26/ball.jpg)**

**Input:** grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
**Output:** [1,-1,-1,-1,-1]
**Explanation:** This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

**Example 2:**

**Input:** grid = [[-1]]
**Output:** [-1]
**Explanation:** The ball gets stuck against the left wall.

**Example 3:**

**Input:** grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
**Output:** [0,1,2,3,4,-1]

---
At first thought, I tried to think if there was a DP solution here that I could use since that's what LeetCode had suggested. Instead I thought about the path that each ball would have to take to reach the bottom. In this case, they always start by coming from above, and then only when there are two boxes in the same direction does it descend down. So if I simulate that by first going to the left or right and then down, I can anticipate when its previous direction was left and it was supposed to be right and vice versa. From there, I could tell where it would land and return the answer from there.

After 30 min, here was my solution

```
```python
class Direction:
  Up = 'Up'
  Down = 'down'
  Right = 'Right'
  Left = 'Left'

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

      def canDescend(i, j, prevDirection):
        if prevDirection == Direction.Right and grid[i][j] == -1:
          return False
        if prevDirection == Direction.Left and grid[i][j] == 1:
          return False

        return True


      def descend(i, j, prevDirection):
        if i < 0 or i > len(grid) or j < 0 or j >= len(grid[0]) or not canDescend(i, j, prevDirection):
          return -1

        if i == len(grid) - 1 and (prevDirection == Direction.Left or prevDirection == Direction.Right ):
          return j

        nextDirection = Direction.Right if grid[i][j] == 1 else Direction.Left
        if prevDirection == Direction.Down:
          if nextDirection == Direction.Right:
            return descend(i, j + 1, nextDirection)
          else:
            return descend(i, j - 1, nextDirection)
        elif prevDirection == Direction.Right and nextDirection == Direction.Right:
            return descend(i + 1, j, Direction.Down)
        elif prevDirection == Direction.Left and nextDirection == Direction.Left:
            return descend(i + 1, j, Direction.Down)


      return [descend(0, x, Direction.Down) for x in range(len(grid[0]))]
```
```


