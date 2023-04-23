[[Interview Question]]
[[Hard]]

A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an `m x n` binary grid `isInfected`, where `isInfected[i][j] == 0` represents uninfected cells, and `isInfected[i][j] == 1` represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two **4-directionally** adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There **will never be a tie**.

Return _the number of walls used to quarantine all the infected regions_. If the world will become fully infected, return the number of walls used.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg)

**Input:** isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
**Output:** 10
**Explanation:** There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
![](https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg)
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
![](https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg)

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg)

**Input:** isInfected = [[1,1,1],[1,0,1],[1,1,1]]
**Output:** 4
**Explanation:** Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

**Example 3:**

**Input:** isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
**Output:** 13
**Explanation:** The region on the left only builds two new walls.

**Constraints:**

-   `m == isInfected.length`
-   `n == isInfected[i].length`
-   `1 <= m, n <= 50`
-   `isInfected[i][j]` is either `0` or `1`.
-   There is always a contiguous viral region throughout the described process that will **infect strictly more uncontaminated squares** in the next round.

---
I spent over 3 hours working on this problem, but finally got to a solution that passed LeetCode. 

The idea is to think about solving the problem in 3 steps.

1. Identify where all the viruses are as well as the extent to which they'll impact the areas around them.
2. After identifying the largest virus, "contain" it by changing the viruses to some non value.
3. Simulate "spreading" the virus by performing another dfs to find its neighbors.

---
Solution:

```python
from pprint import pprint
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
      def isWall(pos, wasGerm):
        x, y = pos
        if x < 0 or x == len(isInfected) or y < 0 or y == len(isInfected[0]):
          return 0
        
        if isInfected[x][y] == 1:
          # is infected and came from germ?
          return 0
        elif isInfected[x][y] == 0 and wasGerm:
          return 1

        return 0
      

      visited = set()
      graph = defaultdict(lambda: [])
      size_graph = defaultdict(lambda: (0, set()))
    
      def explore(pos, isRoot, prevPos, root):
        if pos in visited:
          return

        x, y = pos
        visited.add(pos)
        
        if x < 0 or x == len(isInfected) or y < 0 or y == len(isInfected[0]):
          return
        
        if isInfected[x][y] == 1:
          graph[prevPos].append(pos)
          num_walls = isWall((x, y + 1), True) + isWall((x, y - 1), True)  + isWall((x + 1, y), True)  + isWall((x - 1, y), True) 
          if isWall((x, y + 1), True) == 1:
            size_graph[root][1].add((x, y + 1))
          if isWall((x, y - 1), True) == 1:
            size_graph[root][1].add((x, y - 1))
          if isWall((x + 1, y), True) == 1:
            size_graph[root][1].add((x + 1, y))
          if isWall((x - 1, y), True) == 1:
            size_graph[root][1].add((x - 1, y))
          
          size_graph[root] = (size_graph[root][0] + num_walls, size_graph[root][1])
          explore((x, y + 1), False, pos, root)
          explore((x, y - 1), False, pos, root)
          explore((x + 1, y), False, pos, root)
          explore((x - 1, y), False, pos, root)
      
      

      for x in range(len(isInfected)):
        for y in range(len(isInfected[x])):
          explore((x, y), True, None, (x, y))
      

      max_key, max_seen = None, 0
      for key in size_graph:
        if len(size_graph[key][1]) > max_seen:
          max_seen = len(size_graph[key][1])
          max_key = key
      
      total = 0
      total += size_graph[max_key][0]

      # mark them as seen
      def markContained(root, graph):
        x, y = root
        isInfected[x][y] = -1

        for child in graph[root]:
          markContained(child, graph)
      
      if max_key:
        markContained(max_key, graph)
        graph[None].remove(max_key)

      # move to the next state
      def growVirus(graph, pos):
        x, y = pos
        if isInfected[x][y] == -1:
          return
        if isWall((x, y + 1), True) == 1:
          isInfected[x][ y + 1] = 1
        if isWall((x, y - 1), True) == 1:
          isInfected[x][y - 1] = 1
        if isWall((x + 1, y), True) == 1:
          isInfected[x + 1][y] = 1
        if isWall((x - 1, y), True) == 1:
          isInfected[x- 1][y] = 1


        for child in graph[pos]:
          growVirus(graph, child)

      def advanceToNewDay(graph):
        for root in graph[None]:
          growVirus(graph, root)
      
      def hasNoZeros():
        for x in range(len(isInfected)):
          for y in range(len(isInfected[0])):
            if isInfected[x][y] == 0:
              return False
        return True


      def allVirusContained(graph):
        return len(graph[None]) == 0 or hasNoZeros()

      while not allVirusContained(graph):
        advanceToNewDay(graph)
        size_graph = defaultdict(lambda: (0, set()))
        visited = set()
        roots = graph[None]
        graph = defaultdict(lambda: [])
        for root in roots:
          explore(root, True, None, root)

        max_key, max_seen = None, -1
        for key in size_graph:
          if len(size_graph[key][1]) > max_seen:
            max_seen = len(size_graph[key][1])
            max_key = key
        
        if max_key:
          total += size_graph[max_key][0]
          markContained(max_key, graph)
      
      return total
```
