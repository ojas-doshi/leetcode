# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, freq):
            nonlocal count
            if not node:
                return

            freq[node.val] += 1

            if not node.left and not node.right:
                odd_count = 0
                for f in freq.values():
                    if f % 2 != 0:
                        odd_count += 1
                if odd_count <= 1:
                    count += 1

            dfs(node.left, freq)
            dfs(node.right, freq)

            freq[node.val] -= 1  # Backtrack

        count = 0
        dfs(root, {i: 0 for i in range(1, 10)})
        return count