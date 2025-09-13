class Solution:
    def func(self, nums, ind, ans, curr):
      if ind == len(nums):
        ans.append(sum(curr))
        return

      self.func(nums, ind+1, ans, curr)
      curr.append(nums[ind])
      self.func(nums, ind+1, ans, curr)
      curr.pop()

    def subsetSums(self, nums):
      ans = []
      self.func(nums, 0, ans, [])
      return ans  