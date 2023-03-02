from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

      def balanced(node):

        if node is None:
          return 0, True

        rightHeight, rightBalanced = balanced(node.right)
        leftHeight, leftBalanced = balanced(node.left)

        return max(rightHeight, leftHeight) + 1, abs(rightHeight - leftHeight) <= 1 and rightBalanced and leftBalanced


      return balanced(root)[1]
