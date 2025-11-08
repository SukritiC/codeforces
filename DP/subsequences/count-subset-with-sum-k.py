# Memoization

MODULO = 10 ** 9 + 7
class Solution:
    def func(self, ind, k, n, arr, dp):
        if k == 0:
            return 1
        if ind == 0:
            if arr[ind] == k:
                return 1
            else:
                return 0

        if dp[ind][k] != -1:
            return dp[ind][k]

        not_pick = self.func(ind - 1, k, n, arr, dp)

        pick = False
        if arr[ind] <= k:
            pick = self.func(ind - 1, k - arr[ind], n, arr, dp)

        dp[ind][k] = (pick + not_pick) % MODULO
        return dp[ind][k]

    def perfectSum(self, arr, K):
        n = len(arr)

        dp = [[-1 for _ in range(K + 1)] for _ in range(n)]
        return self.func(n - 1, K, n, arr, dp)

# Tabulation



