from collections import deque


class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True

    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        total = 0
        time = 0
        count = 0
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            size = len(q)
            count += size
            for _ in range(size):
                cell = q.popleft()
                row, col = cell
                for i in range(4):
                    newR = row + self.dx[i]
                    newC = col + self.dy[i]

                    if self.isValid(newR, newC, n, m) and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
            if q:
                time += 1
        if total == count:
            return time
        return -1

