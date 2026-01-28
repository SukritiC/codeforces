class Solution:
    def floorSqrt(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= n:
                low = mid + 1
            else:
                high = mid - 1
        return high

