# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._inorder_leftmost(root)
        
    def _inorder_leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self):
        """
        @return the next smallest number
        """
        if self.hasNext():
            node = self.stack.pop()
            if node.right:
                self._inorder_leftmost(node.right)
            return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()