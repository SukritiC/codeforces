class Solution:
    def func(self, ind, curr, ans, keypad, digits):
        if ind == len(digits):
            ans.append(curr)
            return

        num = int(digits[ind])
        for i in keypad[num]:
            self.func(ind + 1, curr + i,ans, keypad, digits)

    def letterCombinations(self, digits):
        keypad = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                  ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        if not digits:
            return ans
        self.func(0, "", ans, keypad, digits)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("34"))