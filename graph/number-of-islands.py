from collections import deque


class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True

    def bfs(self, i, j, vis, grid):

        vis[i][j] = True
        q = deque()
        q.append((i, j))
        n = len(grid)
        m = len(grid[0])
        while q:
            row, col = q.popleft()
            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    newRow = row + delRow
                    newCol = col + delCol
                    if (self.isValid(newRow, newCol, n, m) and
                            grid[newRow][newCol] == '1' and not vis[newRow][newCol]):
                        vis[newRow][newCol] = True
                        q.append((newRow, newCol))

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        vis = [[False for _ in range(m)] for _ in range(n)]

        count = 0

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, vis, grid)
        return count
