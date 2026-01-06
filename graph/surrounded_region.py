class Solution:
    def __init__(self):
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]

    def isValid(self, row, col, n, m):
        if row < 0 or row >= n:
            return False
        if col < 0 or col >= m:
            return False
        return True

    def dfs(self, row, col, vis, mat, n, m):
        vis[row][col] = True

        for i in range(4):
            nRow = row + self.dx[i]
            nCol = col + self.dy[i]

            if (self.isValid(nRow, nCol, n, m) and mat[nRow][nCol] == 'O' and not vis[nRow][nCol]):
                self.dfs(nRow, nCol, vis, mat, n, m)


    def fill(self, mat):
        n = len(mat)
        m = len(mat[0])

        vis = [[False] * m for _ in range(n)]

        for j in range(m):
            if not vis[0][j] and mat[0][j] =='O':
                self.dfs(0, j, vis, mat, n, m)
            if not vis[n-1][j] and mat[n-1][j] == 'O':
                self.dfs(n-1, j, vis, mat, n, m)
        for i in range(n):
            if not vis[i][0] and mat[i][0] =='O':
                self.dfs(i, 0, vis, mat, n, m)
            if not vis[i][m-1] and mat[i][m-1] == 'O':
                self.dfs(i, m-1, vis, mat, n, m)
        for i in range(n):
            for j in range(m):
                if (mat[i][j] == 'O' and not vis[i][j]):
                    mat[i][j] = 'X'
        return mat