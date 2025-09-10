class Solution:
    def func(self, nums, k, ind, curr, ans):
        if k == 0 and curr not in ans:
            ans.append(curr[:])
            return
        if k < 0 or ind < 0:
            return

        not_pick = self.func(nums, k, ind - 1, curr, ans)
        curr.append(nums[ind])
        pick = self.func(nums, k - nums[ind], ind - 1, curr, ans)

        curr.pop()

    def combinationSum2(self, candidates, target):
        ans = []
        self.func(candidates, target, len(candidates) - 1, [], ans)
        ans = [list(t) for t in set(tuple(sorted(l)) for l in ans)]
        return ans



'''
Optimized code
'''


class Solution:
    def __init__(self):
        self.ans = []

    def func(self, ind, sum, nums, candidates):
        # If the sum is zero, add the current combination to the result
        if sum == 0:
            self.ans.append(nums[:])
            return

        # If the sum is negative or we have exhausted the candidates, return
        if sum < 0 or ind == len(candidates):
            return

        # Include the current candidate
        nums.append(candidates[ind])

        # Recursively call with updated sum and next index
        self.func(ind + 1, sum - candidates[ind], nums, candidates)

        # Backtrack by removing the last added candidate
        nums.pop()

        # Skip duplicates: if not picking the current candidate,
        # ensure the next candidate is different
        for i in range(ind + 1, len(candidates)):
            if candidates[i] != candidates[ind]:
                self.func(i, sum, nums, candidates)
                break

    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort candidates to handle duplicates
        self.ans = []
        self.func(0, target, [], candidates)
        return self.ans
