# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        maxDepth = 0

        def dfs(root: Optional[TreeNode], depth: int) -> None:
            nonlocal ans
            nonlocal maxDepth
            if not root:
                return
            if depth > maxDepth:
                maxDepth = depth
                ans = root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return ans