# Tabulation approach of Climbing stairs

class Solution:

    def climbStairs(self, n):
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



# Space Optimization Approach
class Solution:

    def climbStairs(self, n):
        prev1 = prev2 = 1
        for i in range(2,n+1):
            curr_i = prev1 + prev2
            prev2 = prev1
            prev1 = curr_i

        return prev1