class Solution:
    def findPlatform(self, Arrival, Departure):

        n = len(Arrival)
        Arrival.sort()
        Departure.sort()
        ans = 1
        count = 1
        i, j = 1, 0

        while i < n and j < n:
            if Arrival[i] <= Departure[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
