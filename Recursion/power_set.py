class Solution:
    def func(self, ind, res, current, nums, n):
        if ind == n:
            res.append(current[:])
            return
        #not pick
        self.func(ind+1, res, current, nums, n)

        # pick
        current.append(nums[ind])
        self.func(ind+1, res, current, nums, n)

        current.pop()

    def powerSet(self, nums):
        ans = []
        n = len(nums)
        current = []

        self.func(0, ans, current, nums, n)
        return ans