#Brute force Approach via DP
class Solution(object):
    def func(self, ind, s, count, dp):
        if count < 0:
            return False
        if ind == len(s):
            return count == 0
        if dp[ind][count] != -1:
            return dp[ind][count]

        ans = False
        if s[ind] == '(':
            ans = self.func(ind + 1, s, count + 1, dp)
        elif s[ind] == ')':
            ans = self.func(ind + 1, s, count - 1, dp)
        else:
            for i in range(-1, 2):
                ans = ans or self.func(ind + 1, s, count + i, dp)
        dp[ind][count] = ans
        return ans

    def isValid(self, s):
        n = len(s)

        # DP table
        dp = [[-1] * n for _ in range(n)]
        return self.func(0, s, 0, dp)

# Optimized Approach
class Solution(object):
    '''
    Here we're mainting a range of possible values
    0 - indicates complete balance
    1 - indicates openings are more than closing
    -1 - indicates openings are less than closing
    So instead like above solution opting for the count, we'll opt for the range of possible values
    :return possiblilities [minOpen, maxOpen] if minOpen == 0 return True else False
    '''
    def isValid(self, s):
        minOpen, maxOpen = 0, 0
        for c in s:
            if c == '(':
                minOpen += 1  # Treat as opening
                maxOpen += 1  # Treat as opening
            elif c == ')':
                minOpen -= 1  # Treat as closing
                maxOpen -= 1  # Treat as closing
            elif c == '*':
                minOpen -= 1  # Treat as closing
                maxOpen += 1  # Treat as opening
            if maxOpen < 0:
                return False  # More closing parentheses than opening
            if minOpen < 0:
                minOpen = 0  # Reset minOpen if negative
        return minOpen == 0  # Check if balanced






