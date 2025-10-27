# Memoization
class Solution:
    def func(self, i, j, triangle, n, dp):
        if i == n-1:
            return triangle[i][j]
        if i >= n or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        down = triangle[i][j] + self.func(i+1, j, triangle, n, dp)
        diagonal = triangle[i][j] + self.func(i+1, j+1, triangle, n, dp)

        dp[i][j] = min(down, diagonal)
        return dp[i][j]


    def minTriangleSum(self, triangle):
        n = len(triangle)
        dp = [[-1]* n for _ in range(n)]
        return self.func(0,0, triangle, n, dp)

# Tabulation

class Solution:

    def minTriangleSum(self, triangle):
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[n - 1][j] = triangle[n - 1][j]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                down = triangle[i][j] + dp[i + 1][j]
                diagonal = triangle[i][j] + dp[i + 1][j + 1]

                dp[i][j] = min(down, diagonal)
        return dp[0][0]
