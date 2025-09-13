class Solution:
    def func(self, ind, num, k, n, ans, curr):
        if num > 9 or n < 0:
            return
        if n == 0 and len(curr) == k:
            ans.append(curr[:])
            return

        # not pick
        self.func(ind + 1, num + 1, k, n, ans, curr)

        # pick
        curr.append(num)
        self.func(ind + 1, num + 1, k, n - num, ans, curr)
        curr.pop()

    def combinationSum3(self, k, n):
        ans = []
        self.func(0, 1, k, n, ans, [])
        return ans


if __name__ == "__main__":
    s = Solution()
    ans = s.combinationSum3(4, 15)
    print(ans)