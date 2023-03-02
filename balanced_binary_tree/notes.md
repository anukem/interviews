Given a binary tree, determine if it is 

**height-balanced**

.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**Input:** root = [3,9,20,null,null,15,7]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**Input:** root = [1,2,2,3,3,null,null,4,4]
**Output:** false

**Example 3:**

**Input:** root = []
**Output:** true

---

General intuition here was to recursively iterate over all the nodes and keep track of their depth. When I have the depth of two subtrees, I can compare their relative heights to see if there's a mismatch and propogate that up to the parent. The result is any node who has two imbalanced trees will return False.

Took about 20 minutes, and the solution I came up with was

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

      def balanced(node):

        if node is None:
          return 0, True

        rightHeight, rightBalanced = balanced(node.right)
        leftHeight, leftBalanced = balanced(node.left)

        return max(rightHeight, leftHeight) + 1, abs(rightHeight - leftHeight) <= 1 and rightBalanced and leftBalanced


      return balanced(root)[1]
```
