# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, currSum):
            if not node:
                return 0

            totalPaths = 0
            # Check if the current node value equals the targetSum, if so, increment totalPaths
            if node.val == currSum:
                totalPaths += 1

            # Recursively check left and right subtrees with updated targetSum
            totalPaths += dfs(node.left, currSum - node.val)
            totalPaths += dfs(node.right, currSum - node.val)

            return totalPaths

        if not root:
            return 0

        # Start traversal from the root node
        pathsFromRoot = dfs(root, targetSum)

        # Recursively check left and right subtrees
        pathsFromLeft = self.pathSum(root.left, targetSum)
        pathsFromRight = self.pathSum(root.right, targetSum)

        # Total paths will be the sum of paths from root, left, and right subtrees
        return pathsFromRoot + pathsFromLeft + pathsFromRight