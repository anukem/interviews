class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return "Node: " + str(self.val) + "\n(" + str(self.left) + "," + str(self.right) + ")"

    def __str__(self) -> str:
        return "Node: " + str(self.val) + "\n(" + str(self.left) + "," + str(self.right) + ")"

class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result


def convertArrayToNodes(arr):
    parents = {}
    for i, elem in enumerate(arr):
        if elem == None:
            continue
        arr[i] = TreeNode(elem)
        parents[(i*2) + 1] = i, 'l'
        parents[(i*2) + 2] = i, 'r'

    for i, elem in enumerate(arr):
        if i in parents:
            if parents[i][1] == 'l':
                arr[parents[i][0]].left = elem
            else:
                arr[parents[i][0]].right = elem


    return arr

nodes = convertArrayToNodes([10,5,-3,3,2,None,11,3,-2,None,1])

Solution().pathSum(nodes[0], 8)


