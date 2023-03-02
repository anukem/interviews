[[Interview Question]]
[Medium]

Given the `root` of a binary tree and an integer `targetSum`, return _the number of paths where the sum of the values along the path equals_ `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

**Input:** root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
**Output:** 3
**Explanation:** The paths that sum to 8 are shown.

**Example 2:**

**Input:** root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
**Output:** 3

---
My original solution involved iterating over each path with DFS, and storing both the value up until the node that I'm currently on, as well as a new path that starts from the node I'm currently on. If I encounter a node that is able to add up to the sum of the target, then I can add to some global state and continue iterating. The key insight here is that only storing the value accrued up until a certain node is all you need to be able to figure out whether or not the target can be achieved at that node. This is because subtracting the target from the accrued value will either land you on some artibrary node before, or it won't. And if it does, then you can add all the times that that value has been seen before reaching the current node.

My solution is as follows:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

      total = []

      def traverse(node, targetNums):

        if node is None:
          return

        if node.val == targetSum:
          total.append(1)

        newTargets = []
        for num in targetNums:
          if num + node.val == targetSum:
            total.append(1)

          newTargets.append(num + node.val)



        newTargets.append(node.val)

        traverse(node.left, newTargets)
        traverse(node.right, newTargets)

      traverse(root, [])

      return len(total)
```

And the optimized solution is here:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

      total = []

      def traverse(node, targetNums):

        if node is None:
          return

        if node.val == targetSum:
          total.append(1)

        newTargets = []
        for num in targetNums:
          if num + node.val == targetSum:
            total.append(1)

          newTargets.append(num + node.val)



        newTargets.append(node.val)

        traverse(node.left, newTargets)
        traverse(node.right, newTargets)

      traverse(root, [])

      return len(total)
```


