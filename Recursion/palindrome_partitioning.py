class Solution:
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def func(self, ind, curr, ans, s):
        if ind == len(s):
            ans.append(curr[:])
            return

        for j in range(ind, len(s)):
            if (self.isPalindrome(s, ind, j)):
                val = s[ind:j + 1]
                curr.append(val)
                self.func(j + 1, curr, ans, s)
                curr.pop()

    def partition(self, s: str):
        ans = []
        self.func(0, [], ans, s)
        return ans