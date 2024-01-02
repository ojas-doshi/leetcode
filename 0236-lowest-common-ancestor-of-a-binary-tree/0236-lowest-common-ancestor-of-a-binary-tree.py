# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, target, path):
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if (dfs(node.left, target, path) or dfs(node.right, target, path)):
                return True

            path.pop()
            return False

        path_p = []
        path_q = []

        dfs(root, p, path_p)
        dfs(root, q, path_q)

        lca = None
        for node_p, node_q in zip(path_p, path_q):
            if node_p == node_q:
                lca = node_p
            else:
                break

        return lca