class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        return self.construct_quad_tree(grid, 0, 0, len(grid))

    def construct_quad_tree(self, grid, x, y, size):
        if size == 1:
            return Node(grid[x][y] == 1, True)

        half = size // 2

        topLeft = self.construct_quad_tree(grid, x, y, half)
        topRight = self.construct_quad_tree(grid, x, y + half, half)
        bottomLeft = self.construct_quad_tree(grid, x + half, y, half)
        bottomRight = self.construct_quad_tree(grid, x + half, y + half, half)

        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True)
        else:
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
