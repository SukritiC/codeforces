# Tabulation Approach
class Solution:

    def frogJump(self, heights):
        n = len(heights)
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n):
            oneStep = dp[i - 1] + abs(heights[i] - heights[i - 1])
            twoStep = float('inf')
            if i > 1:
                twoStep = dp[i - 2] + abs(heights[i] - heights[i - 2])
            dp[i] = min(oneStep, twoStep)

        return dp[n - 1]


# Space Optimization Approach
class Solution:

    def frogJump(self, heights):
        n = len(heights)

        prev1 = 0
        prev2 = 0

        for i in range(1, n):
            oneStep = prev1 + abs(heights[i] - heights[i - 1])
            twoStep = float('inf')
            if i > 1:
                twoStep = prev2 + abs(heights[i] - heights[i - 2])

            curr_i = min(oneStep, twoStep)
            prev2 = prev1
            prev1 = curr_i

        return prev1

