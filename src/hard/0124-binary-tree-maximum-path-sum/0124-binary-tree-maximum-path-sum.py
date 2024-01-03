# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumHelper(node):
            nonlocal max_sum
            if not node:
                return 0

            # Calculate the maximum path sum in the left and right subtrees
            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))

            # Update the global maximum path sum considering the current node
            max_sum = max(max_sum, node.val + left_sum + right_sum)

            # Return the maximum path sum starting from the current node
            return node.val + max(left_sum, right_sum)

        max_sum = float('-inf')  # Initialize the global maximum path sum
        maxPathSumHelper(root)
        return max_sum