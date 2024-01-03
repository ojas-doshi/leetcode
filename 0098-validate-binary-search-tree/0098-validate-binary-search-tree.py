# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node, inorder_list):
            if node is None:
                return
            inorder_traversal(node.left, inorder_list)
            inorder_list.append(node.val)
            inorder_traversal(node.right, inorder_list)

        inorder_list = []
        inorder_traversal(root, inorder_list)

        # Check if the inorder list is sorted
        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i - 1]:
                return False

        return True