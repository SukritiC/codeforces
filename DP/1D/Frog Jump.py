class Solution:
    def func(self, n, heights, dp):
        if n < 0:
            return
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]

        one_step = self.func(n - 1, heights, dp) + abs(heights[n] - heights[n - 1])
        two_step = float('inf')
        if n > 1:
            two_step = self.func(n - 2, heights, dp) + abs(heights[n] - heights[n - 2])

        dp[n] = min(one_step, two_step)
        return dp[n]

    def frogJump(self, heights):
        n = len(heights)
        dp = [-1] * (n + 1)
        return self.func(n - 1, heights, dp)