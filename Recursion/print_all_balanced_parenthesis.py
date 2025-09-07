class Solution:
    '''
    The objetive was to print all possible combinations for n pairs of parentheses
    '''
    def func(self, val, op, cl, ans, n):
            if op == cl == n:
                ans.append(val)
                return
            if op < n :
                self.func(val + "(", op+1, cl, ans, n)
            if op > cl:
                self.func(val+ ")", op, cl+1, ans, n)
    def generateParenthesis(self, n):
        ans = []
        self.func( "", 0, 0, ans, n)
        return ans