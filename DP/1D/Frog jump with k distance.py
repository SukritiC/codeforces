class Solution:
    def func(self, n, heights, k, dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]

        min_steps = float('inf')
        for j in range(1, k+1):
            if n -j >= 0:
                jump = self.func(n-j, heights, k, dp) + abs(heights[n] - heights[n-j])
                min_steps = min(jump, min_steps)

        dp[n] = min_steps
        return dp[n]

    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1]*(n+1)

        return self.func(n-1, heights, k, dp)
