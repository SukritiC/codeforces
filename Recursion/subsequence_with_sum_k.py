class Solution:
    '''
    Recursion Solution
    '''
    def func(self, nums, k, n, sum_val, ind):
        if sum_val == k:
            return True
        if ind == n or sum_val > k:
            return sum_val == k

        not_pick = self.func(nums, k, n, sum_val, ind + 1)

        pick = self.func(nums, k, n, sum_val + nums[ind], ind + 1)
        return pick or not_pick

    def checkSubsequenceSum(self, nums, k):
        return self.func(nums, k, len(nums), 0, 0)


    # DP Solution

    def func(self, nums, k, n, sum_val, ind, dp):
        if sum_val == k:
            return True
        if ind == n or sum_val > k:
            return sum_val == k

        if dp[ind][sum_val] is not None:
            return dp[ind][sum_val]

        pick = self.func(nums, k, n, sum_val + nums[ind], ind + 1, dp)

        not_pick = self.func(nums, k, n, sum_val, ind + 1, dp)

        dp[ind][sum_val] = pick or not_pick
        return dp[ind][sum_val]

    def checkSubsequenceSum(self, nums, k):
        dp = [[None for _ in range(k + 1)] for _ in range(n)]
        return self.func(nums, k, n, 0, 0, dp)
