# Memoization
class Solution:
    def func(self, i, j, m, matrix, dp):
        if j < 0 or j >= m:
            return int(1e9)
        if i == 0:
            return matrix[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        up = matrix[i][j] + self.func(i - 1, j, m, matrix, dp)
        left_d = matrix[i][j] + self.func(i - 1, j - 1, m, matrix, dp)
        right_d = matrix[i][j] + self.func(i - 1, j + 1, m, matrix, dp)

        dp[i][j] = min(up, min(left_d, right_d))
        return dp[i][j]

    def minFallingPathSum(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        dp = [[-1] * m for _ in range(n)]
        min_val = float('inf')

        for j in range(m):
            ans = self.func(n - 1, j, m, matrix, dp)
            min_val = min(ans, min_val)

        return min_val

# Tabulation
class Solution:
    def func(self, i, j, m, matrix, dp):
        if j < 0 or j >= m:
            return int(1e9)
        if i == 0:
            return matrix[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        up = matrix[i][j] + self.func(i - 1, j, m, matrix, dp)
        left_d = matrix[i][j] + self.func(i - 1, j - 1, m, matrix, dp)
        right_d = matrix[i][j] + self.func(i - 1, j + 1, m, matrix, dp)

        dp[i][j] = min(up, min(left_d, right_d))
        return dp[i][j]

    def minFallingPathSum(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        dp = [[-1] * m for _ in range(n)]
        min_val = float('inf')

        for j in range(m):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(m):

                up = matrix[i][j] + dp[i - 1][j]

                left_d = matrix[i][j]
                if j - 1 >= 0:
                    left_d += dp[i - 1][j - 1]
                else:
                    left_d += float('inf')

                right_d = matrix[i][j]
                if j + 1 < m:
                    right_d += dp[i - 1][j + 1]
                else:
                    right_d += float('inf')

                dp[i][j] = min(up, min(left_d, right_d))

        mini = float('inf')
        for j in range(m):
            mini = min(mini, dp[n - 1][j])

        return mini