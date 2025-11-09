# memoization

class Solution:
    def func(self, ind, wt, val, n, W, dp):
        if W == 0:
            return 0
        if ind == 0:
            if wt[ind] <= W:
                return val[ind]
            else:
                return 0
        if dp[ind][W] != -1:
            return dp[ind][W]

        not_pick = 0 + self.func(ind - 1, wt, val, n, W, dp)
        pick = False
        if wt[ind] <= W:
            pick = val[ind] + self.func(ind - 1, wt, val, n, W - wt[ind], dp)

        dp[ind][W] = max(not_pick, pick)
        return dp[ind][W]

    def knapsack01(self, wt, val, n, W):
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.func(n - 1, wt, val, n, W, dp)

