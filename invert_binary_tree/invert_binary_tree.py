from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root is None:
                return None

            right = invert(root.right)
            left = invert(root.left)
            root.right = left
            root.left = right

            return root

        return invert(root)
