from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            if j + 1 < cols and grid[i][j + 1] == INF:
                grid[i][j + 1] = grid[i][j] + 1
                q.append((i, j + 1))
            if j - 1 >= 0 and grid[i][j - 1] == INF:
                grid[i][j - 1] = grid[i][j] + 1
                q.append((i, j - 1))
            if i + 1 < rows and grid[i + 1][j] == INF:
                grid[i + 1][j] = grid[i][j] + 1
                q.append((i + 1, j))
            if i - 1 >= 0 and grid[i - 1][j] == INF:
                grid[i - 1][j] = grid[i][j] + 1
                q.append((i - 1, j))