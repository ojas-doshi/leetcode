# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            # The size variable will keep track of the number of nodes at each level
            size = len(queue)

            # Iterating through all the nodes at the current level
            for i in range(size):
                node = queue.pop(0)

                # Add the rightmost node value of the current level to the result
                if i == size - 1:
                    result.append(node.val)

                # Add the child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result