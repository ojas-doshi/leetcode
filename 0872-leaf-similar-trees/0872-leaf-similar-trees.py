# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_sequence(root, sequence):
            if not root:
                return
            if not root.left and not root.right:
                sequence.append(root.val)
                return
            get_leaf_sequence(root.left, sequence)
            get_leaf_sequence(root.right, sequence)

        leaf_sequence_1 = []
        leaf_sequence_2 = []

        get_leaf_sequence(root1, leaf_sequence_1)
        get_leaf_sequence(root2, leaf_sequence_2)

        return leaf_sequence_1 == leaf_sequence_2