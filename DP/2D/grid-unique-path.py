# memoization

class Solution:
    def func(self, i, j, dp):
        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.func(i - 1, j, dp)
        left = self.func(i, j - 1, dp)

        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.func(m - 1, n - 1, dp)

# Tabulation

class Solution:
    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Base condition
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

        return dp[m - 1][n - 1]

# Space Optimization

class Solution:
    
    def uniquePaths(self, m, n):
        prev_row = [0] * n
        for i in range(m):
            curr_row = [0] * n
            for j in range(n):
                # base case
                if i == 0 and j == 0:
                    curr_row[j] = 1
                    continue

                up = prev_row[j] if i > 0 else 0
                left = curr_row[j - 1] if j > 0 else 0

                curr_row[j] = up + left
            prev_row = curr_row

        return prev_row[-1]

