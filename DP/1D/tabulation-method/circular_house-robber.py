# Optimal Solution
class Solution:

    def func(self, nums):
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

    def houseRobber(self, money):
        n = len(money)
        if n == 0:
            return 0
        if n == 1:
            return money[0]

        # Exclude last element
        arr1 = money[:-1]

        # Exclude first element
        arr2 = money[1:]

        ans1 = self.func(arr1)
        ans2 = self.func(arr2)

        # Return the maximum of ans1 and ans2
        return max(ans1, ans2)
