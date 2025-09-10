class Solution:
    def func(self, ind, nums, k):
        if k == 0:
            return 1
        if k < 0 or ind == len(nums):
            return 0
        pick = self.func(ind + 1, nums, k - nums[ind])
        not_pick = self.func(ind + 1, nums, k)
        return pick + not_pick

    def countSubsequenceWithTargetSum(self, nums, k):
        return self.func(0, nums, k)

    # DP
    class Solution:
        def func(self, ind, nums, k, memo):
            if k == 0:
                return 1
            if k < 0 or ind == len(nums):
                return 0
            if (ind, k) in memo:
                return memo[(ind, k)]

            pick = self.func(ind + 1, nums, k - nums[ind], memo)
            not_pick = self.func(ind + 1, nums, k, memo)

            memo[(ind, k)] = pick + not_pick
            return memo[(ind, k)]

        def countSubsequenceWithTargetSum(self, nums, k):
            memo = {}
            return self.func(0, nums, k, memo)