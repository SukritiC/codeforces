class Solution:
    def nthRoot(self, num, n):
        root = 1
        for i in range(n):
            root *= num
        return root

    def NthRoot(self, n, m):
        low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2

            val = self.nthRoot(mid, n)
            if val == m:
                return mid
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1


