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


if __name__ == "__main__":
    s = Solution()
    ans = s.powerSet([5,1,3,1])


    print(ans)
    print(len(ans))
