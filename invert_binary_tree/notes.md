[[Interview Question]]
[Easy]
Given the `root` of a binary tree, invert the tree, and return _its root_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

**Input:** root = [2,1,3]
**Output:** [2,3,1]

**Example 3:**

**Input:** root = []
**Output:** []

---

Approach seemed pretty straightforward. Start by getting the value of the root, and then inverting the left and right sub trees respectively. Once that's done, you can return the root.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

      
      def invert(root):
        if root == None:
          return None
        
        right = invert(root.right)
        left = invert(root.left)
        root.right = left
        root.left = right

        return root
        

      return invert(root)
```

