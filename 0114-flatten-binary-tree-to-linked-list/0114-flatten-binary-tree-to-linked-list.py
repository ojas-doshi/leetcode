# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def flatten_helper(node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            left_last = flatten_helper(node.left)
            right_last = flatten_helper(node.right)

            if left_last:
                left_last.right = node.right
                node.right = node.left
                node.left = None

            return right_last if right_last else left_last

        flatten_helper(root)