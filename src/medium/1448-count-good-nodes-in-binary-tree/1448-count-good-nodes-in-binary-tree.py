# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_good_nodes(node, max_val):
            if not node:
                return 0

            # Check if the current node is a good node
            is_good = node.val >= max_val
            # Update the maximum value encountered in the path
            new_max_val = max(max_val, node.val)

            # Recursively check left and right subtrees
            left_count = count_good_nodes(node.left, new_max_val)
            right_count = count_good_nodes(node.right, new_max_val)

            # Return the count of good nodes in left and right subtrees
            return (1 if is_good else 0) + left_count + right_count

        return count_good_nodes(root, float('-inf'))