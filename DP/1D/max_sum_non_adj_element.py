class Solution:
    def func(self, n, nums, dp):
        if n==0:
            return nums[0]
        if n<0:
            return 0
        if dp[n] != -1:
            return dp[n]

        pick = nums[n] + self.func(n-2, nums, dp)

        not_pick = self.func(n-1, nums, dp)
        dp[n] = max(pick, not_pick)
        return dp[n]

    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1] * (n+1)
        return self.func(n-1, nums, dp)