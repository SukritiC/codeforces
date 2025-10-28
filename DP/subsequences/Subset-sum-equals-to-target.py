# memoization
class Solution:
    def func(self, ind, target, arr, dp):
        if target == 0:
            return True
        if ind == 0:
            return arr[0] == target
        if dp[ind][target] != -1:
            return dp[ind][target]

        notPick = self.func(ind - 1, target, arr, dp)

        pick = False
        if arr[ind] <= target:
            pick = self.func(ind - 1, target - arr[ind], arr, dp)

        dp[ind][target] = 1 if notPick or pick else 0
        return dp[ind][target]

    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        return self.func(n - 1, target, arr, dp)

# Tabulation

class Solution:

    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                notPick = dp[i - 1][j]

                pick = False
                if arr[i] <= j:
                    pick = dp[i - 1][j - arr[i]]

                dp[i][j] = pick or notPick

        return dp[n - 1][target]


