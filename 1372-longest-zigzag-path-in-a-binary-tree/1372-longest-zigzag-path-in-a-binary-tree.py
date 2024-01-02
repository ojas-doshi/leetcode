# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    max_length = 0

    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, direction, length):
            if not node:
                return
            
            self.max_length = max(self.max_length, length)
            
            if direction == 'left':
                dfs(node.left, 'right', length + 1)
                dfs(node.right, 'left', 1)
            else:
                dfs(node.right, 'left', length + 1)
                dfs(node.left, 'right', 1)
        
        if not root:
            return 0
        
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)

        return  self.max_length