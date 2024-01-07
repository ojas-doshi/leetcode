# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal prev_val, min_diff
            if node:
                inorder(node.left)
                if prev_val is not None:
                    min_diff = min(min_diff, node.val - prev_val)
                prev_val = node.val
                inorder(node.right)

        prev_val = None
        min_diff = float('inf')
        inorder(root)
        return min_diff