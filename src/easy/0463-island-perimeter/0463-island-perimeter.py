class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Assume 4 sides initially
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2  # Subtract 2 if the top cell is land
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2  # Subtract 2 if the left cell is land

        return perimeter