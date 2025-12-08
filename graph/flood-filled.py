class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True

    def dfs(self, row, col, ans, image, newColor, initial_color):
        ans[row][col] = newColor
        n = len(image)
        m = len(image[0])

        for i in range(4):
            nrow = row + self.delRow[i]
            ncol = col + self.delCol[i]

            if (
                    self.isValid(nrow, ncol, n, m) and image[nrow][ncol] == initial_color
                    and ans[nrow][ncol] != newColor):
                self.dfs(nrow, ncol, ans, image, newColor, initial_color)

    def floodFill(self, image, sr, sc, newColor):
        initial_color = image[sr][sc]
        ans = [row[:] for row in image]

        self.dfs(sr, sc, ans, image, newColor, initial_color)
        return ans