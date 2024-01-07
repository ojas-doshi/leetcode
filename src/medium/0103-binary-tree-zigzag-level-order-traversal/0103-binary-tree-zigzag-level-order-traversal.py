# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True  # Flag for traversal direction

        while queue:
            level_values = []
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level_values = level_values[::-1]  # Reverse the level values if needed

            result.append(level_values)
            left_to_right = not left_to_right  # Toggle the traversal direction for the next level

        return result