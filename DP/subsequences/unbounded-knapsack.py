class Solution:
    def func(self, wt, val, ind, W, dp):
        if W == 0:
            return 0
        if ind == 0:
            return (W // wt[0]) * val[0]

        if dp[ind][W] != -1:
            return dp[ind][W]

        not_pick = self.func(wt, val, ind - 1, W, dp)
        pick = 0
        if wt[ind] <= W:
            pick = val[ind] + self.func(wt, val, ind, W - wt[ind], dp)

        dp[ind][W] = max(not_pick, pick)
        return dp[ind][W]

    def unboundedKnapsack(self, wt, val, n, W):
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]

        return self.func(wt, val, n - 1, W, dp)
