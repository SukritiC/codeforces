class Solution:
    def func(self, n, dp):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if dp[n] != -1:
            return dp[n]

        one_step = self.func(n - 1, dp)
        two_step = self.func(n - 2, dp)

        dp[n] = one_step + two_step
        return dp[n]

    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        return self.func(n, dp)