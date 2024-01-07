# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to build the tree recursively
        def buildTreeHelper(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None

            # The last element in postorder is the root of the subtree
            root_val = postorder[post_right]
            root = TreeNode(root_val)

            # Find the index of the root value in inorder array
            inorder_index = index_map[root_val]
            left_subtree_size = inorder_index - in_left

            # Recursively build left and right subtrees
            root.left = buildTreeHelper(in_left, inorder_index - 1, post_left, post_left + left_subtree_size - 1)
            root.right = buildTreeHelper(inorder_index + 1, in_right, post_left + left_subtree_size, post_right - 1)

            return root

        # Start the tree construction
        return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)
