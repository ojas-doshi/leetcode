# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update diameter if the sum of left and right subtree depths is greater
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the maximum depth of the current node
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.diameter