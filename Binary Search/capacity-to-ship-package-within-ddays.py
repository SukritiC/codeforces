class Solution(object):
    def canShip(self, weights, k, days):
        curr = 0
        d = 0
        for i in range(len(weights)):
            if curr + weights[i] <= k:
                curr += weights[i]
            else:
                curr = 0
                d += 1

        return d

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = 1
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            day_used = self.canShip(weights, mid, days)
            if day_used == days:
                return mid
            elif day_used > days:
                low = mid + 1
            else:
                high = mid - 1
        return


if __name__ == "__main__":
    s = Solution()
    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(s.shipWithinDays([3,2,2,4,1,4], 3))