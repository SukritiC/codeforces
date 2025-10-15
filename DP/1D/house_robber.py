# Memoization Technique
class Solution:
    def func(self, n, money, dp):
        if n == 0:
            return money[n]
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]

        # pick
        pick = money[n] + self.func(n - 2, money, dp)

        # not pick
        not_pick = self.func(n - 1, money, dp)

        dp[n] = max(pick, not_pick)
        return dp[n]

    def houseRobber(self, money):
        n = len(money)
        if n == 0:
            return 0
        if n == 1:
            return money[0]

        dp1 = [-1] * (n)
        dp2 = [-1] * (n)

        # exclude the last element in the array
        arr1 = money[:-1]

        # exclude the first element in the Array
        arr2 = money[1:]

        ans1 = self.func(len(arr1) - 1, arr1, dp1)
        ans2 = self.func(len(arr2) - 1, arr2, dp2)

        return max(ans1, ans2)

# Tabulation Technique


