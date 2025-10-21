# Tabulation Approach
class Solution:

    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0] = nums[0]
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            nonPick = dp[i - 1]

            dp[i] = max(pick, nonPick)

        return dp[n - 1]

# Space Optimization Approach
class Solution:

    def nonAdjacent(self, nums):
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            nonPick = prev1

            curr_i = max(pick, nonPick)
            prev2 = prev1
            prev1 = curr_i

        return prev1