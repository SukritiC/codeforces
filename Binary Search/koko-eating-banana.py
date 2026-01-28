import math
class Solution(object):
    def compSum(self, piles, k):
        summ = 0
        for i in range(len(piles)):
            summ += math.ceil(piles[i] / k)
        # print("------",summ)
        return summ

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        # print(high)
        while low <= high:
            mid = (low + high) // 2

            summ = self.compSum(piles, mid)
            if summ <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11], 8))
    print(s.minEatingSpeed([30,11,23,4,20], 5))
    print(s.minEatingSpeed([30,11,23,4,20], 6))
