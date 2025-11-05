# Tabulation
class Solution:

    def equalPartition(self, n, arr):
        sum_val = 0
        for i in arr:
            sum_val += i

        if sum_val % 2 != 0:
            return False
        target = int(sum_val / 2)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):

                not_pick = dp[i - 1][j]

                pick = False
                if arr[i] <= j:
                    pick = dp[i - 1][j - arr[i]]

                dp[i][j] = pick or not_pick
        return dp[n - 1][target]

