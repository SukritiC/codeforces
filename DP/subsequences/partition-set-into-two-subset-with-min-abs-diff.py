class Solution:
    def func(self, ind, target, arr, dp):
        if target == 0:
            dp[ind][target] = True
            return True

        if ind == 0:
            dp[ind][target] = (arr[0] == target)
            return dp[ind][target]

        if dp[ind][target] != -1:
            return dp[ind][target]

        not_taken = self.func(ind - 1, target, arr, dp)
        taken = 0
        if arr[ind] <= target:
            taken = self.func(ind - 1, target - arr[ind], arr, dp)

        dp[ind][target] = not_taken or taken
        return dp[ind][target]

    def minDifference(self, arr, n):
        sum_val = 0
        for i in arr:
            sum_val += i

        dp = [[-1 for _ in range(sum_val + 1)] for _ in range(n)]

        for i in range(sum_val + 1):
            dummy = self.func(n - 1, i, arr, dp)

        mini = float('inf')
        for i in range(sum_val + 1):
            if dp[n - 1][i] == True:
                diff = abs(i - (sum_val - i))
                mini = min(mini, diff)
        return mini

