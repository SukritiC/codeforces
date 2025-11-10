class Solution:
    def func(self, ind, amount, coins, n, dp):
        if ind == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return int(1e9)
        if dp[ind][amount] != -1:
            return dp[ind][amount]

        not_pick = self.func(ind - 1, amount, coins, n, dp)
        pick = int(1e9)
        if coins[ind] <= amount:
            pick = 1 + self.func(ind, amount - coins[ind], coins, n, dp)

        dp[ind][amount] = min(pick, not_pick)
        return dp[ind][amount]

    def MinimumCoins(self, coins, amount):
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        ans = self.func(n - 1, amount, coins, n, dp)
        if ans >= int(1e9):
            return -1
        return ans