class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten = deque()

        # Count fresh oranges and store the positions of rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rotten and fresh_oranges > 0:
            size = len(rotten)
            for _ in range(size):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        rotten.append((nx, ny))
            minutes += 1

        return minutes if fresh_oranges == 0 else -1