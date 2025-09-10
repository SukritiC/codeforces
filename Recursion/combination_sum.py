class Solution:
    def func(self, ind, nums, k, ans, curr):
        if k == 0:
            ans.append(curr[:])
            return

        if k < 0 or ind < 0:
            return

        self.func(ind - 1, nums, k, ans, curr)
        curr.append(nums[ind])
        self.func(ind, nums, k - nums[ind], ans, curr)

        curr.pop()

    def combinationSum(self, candidates, target):
        ans = []
        current = []
        v = candidates[:]
        self.func(len(v) - 1, v, target, ans, current)
        return ans