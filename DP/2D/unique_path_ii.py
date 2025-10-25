# Memoization
class Solution:
    def func(self, i, j, matrix, dp):
        if i < 0 or j < 0 or matrix[i][j] == 1:
            return 0
        elif i == 0 and j == 0:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.func(i - 1, j, matrix, dp)
        left = self.func(i, j - 1, matrix, dp)

        dp[i][j] = up + left
        return dp[i][j]

    def uniquePathsWithObstacles(self, matrix):
        m, n = len(matrix), len(matrix[0])

        dp = [[-1] * n for _ in range(m)]

        return self.func(m - 1, n - 1, matrix, dp)

# Tabulation
    def uniquePathsWithObstacles(self, matrix):
        n, m = len(matrix), len(matrix[0])

        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):

                # Base conditions
                if matrix[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                up = 0
                left = 0

                if i > 0:
                    up = dp[i - 1][j]
                if j > 0:
                    left = dp[i][j - 1]

                dp[i][j] = up + left

        return dp[n - 1][m - 1]