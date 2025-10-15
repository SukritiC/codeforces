class Solution:
    '''
    To buy and sell stocks only 2 time following the consecutive buy and sell sequence
    '''
    def func(self, i, buy, n, arr, dp, cap):
        if i == n:
            return 0
        if cap == 0:
            return 0

        if dp[i][buy][cap] != -1:
            return dp[i][buy][cap]

        profit = 0
        if buy == 0:
            profit = max(((-1) * arr[i] + self.func(i + 1, 1, n, arr, dp, cap), self.func(i + 1, 0, n, arr, dp, cap)))
        if buy == 1:
            profit = max((arr[i] + self.func(i + 1, 0, n, arr, dp, cap-1), self.func(i + 1, 1, n, arr, dp, cap)))

        dp[i][buy][cap] = profit
        return dp[i][buy][cap]

    def stockBuySell(self, arr, n):
        if n == 0:
            return 0

        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return self.func(0, 0, n, arr, dp, 2)

