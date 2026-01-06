from collections import deque


class Solution:
    def isValid(self, row, col, n, m):
        if row < 0 or row >= n:
            return False
        elif col < 0 or col >= m:
            return False
        return True

    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    vis[i][j] = 1
                    q.append((i, j, 0))
                else:
                    vis[i][j] = 0

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while q:
            row, col, step = q.popleft()
            dist[row][col] = step

            for k in range(4):
                nRow = row + dx[k]
                nCol = col + dy[k]
                if self.isValid(nRow, nCol, n, m) and vis[nRow][nCol] == 0:
                    vis[nRow][nCol] = 1
                    q.append((nRow, nCol, step + 1))

        return dist

