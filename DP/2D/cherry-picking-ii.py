class Solution:
    def func(self, i, j1, j2, n, m, matrix, dp):
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return int(-1e9)

        if i == n - 1:
            if j1 == j2:
                return matrix[i][j1]
            else:
                return matrix[i][j1] + matrix[i][j2]

        """ If the result for these indices has
        already been computed, return it"""
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = int(-1e9)

        # Try all possible moves for both positions (j1, j2)
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ans = 0

                if j1 == j2:
                    ans = matrix[i][j1] + self.func(i + 1, j1 + di, j2 + dj, n, m, matrix, dp)
                else:
                    ans = matrix[i][j1] + matrix[i][j2] + self.func(i + 1, j1 + di, j2 + dj, n, m, matrix, dp)

                # Update the maximum result
                maxi = max(maxi, ans)

        """ Store the maximum cherries 
        collected in the memoization table"""
        dp[i][j1][j2] = maxi
        return maxi

    def cherryPickup(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        return self.func(0, 0, m - 1, n, m, matrix, dp)

# Tabulation

class Solution:


    def cherryPickup(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # base case - adding value for j1 --> 0 to m-1 & j2 --> 0 to m-1

        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n - 1][j1][j2] = matrix[n - 1][j1]
                else:
                    dp[n - 1][j1][j2] = matrix[n - 1][j1] + matrix[n - 1][j2]

        for i in range(n - 2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    max_value = int(-1e9)
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            ans = 0
                            if j1 == j2:
                                ans = matrix[i][j1]
                            else:
                                ans = matrix[i][j1] + matrix[i][j2]

                            if (j1 + dj1 < 0 or j1 + dj1 >= m) or (j2 + dj2 < 0 or j2 + dj2 >= m):
                                ans += -1e9
                            else:
                                ans += + dp[i + 1][j1 + dj1][j2 + dj2]
                            max_value = max(ans, max_value)
                    dp[i][j1][j2] = max_value

        return dp[0][0][m - 1]













