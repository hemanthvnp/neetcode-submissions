class Solution:
    def bfs(self, i, j, l1, l2, area):
        if i+1 < len(l1) and j < len(l1[i+1]) and l1[i+1][j] == 1 and (i+1, j) not in l2:
            l2.add((i+1, j))
            area += self.bfs(i+1, j, l1, l2, 1)

        if i-1 >= 0 and j < len(l1[i-1]) and l1[i-1][j] == 1 and (i-1, j) not in l2:
            l2.add((i-1, j))
            area += self.bfs(i-1, j, l1, l2, 1)

        if i < len(l1) and j-1 >= 0 and l1[i][j-1] == 1 and (i, j-1) not in l2:
            l2.add((i, j-1))
            area += self.bfs(i, j-1, l1, l2, 1)

        if i < len(l1) and j+1 < len(l1[i]) and l1[i][j+1] == 1 and (i, j+1) not in l2:
            l2.add((i, j+1))
            area += self.bfs(i, j+1, l1, l2, 1)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        area = 0
        l = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 or (i, j) in l:
                    continue
                else:
                    l.add((i, j))
                    area = self.bfs(i, j, grid, l, 1)
                    maxarea = max(area, maxarea)

        return maxarea