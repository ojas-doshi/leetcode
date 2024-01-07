# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def depth(node):
            count = 0
            while node:
                count += 1
                node = node.left
            return count

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if left_depth == right_depth:
            # Last level is completely filled, return total nodes using formula
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Last level is not completely filled, count nodes recursively
            return (1 << right_depth) + self.countNodes(root.left)
