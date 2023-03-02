from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

      seen = set()
      def traverse(node):

        if node is None:
          return 0

        if not node.left and not node.right:
          seen.add(0)
          return 1


        left = traverse(node.left)
        right = traverse(node.right)

        seen.add(left + right)

        return max(left, right) + 1

      traverse(root)

      return max(seen)

