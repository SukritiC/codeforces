class Solution:
    '''
    To buy and sell stocks infinite number of times, only catch is that can't do consecutive Buys or sells
    '''
    def func(self, i, buy, n, arr, dp):
        if i == n:
            return 0

        if dp[i][buy] != -1:
            return dp[i][buy]

        profit = 0
        if buy == 0:
            profit = max(((-1) * arr[i] + self.func(i + 1, 1, n, arr, dp), self.func(i + 1, 0, n, arr, dp)))
        if buy == 1:
            profit = max((arr[i] + self.func(i + 1, 0, n, arr, dp), self.func(i + 1, 1, n, arr, dp)))

        dp[i][buy] = profit
        return dp[i][buy]

    def stockBuySell(self, arr, n):
        if n == 0:
            return 0

        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.func(0, 0, n, arr, dp)


