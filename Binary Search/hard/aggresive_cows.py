class Solution:
    def canWePlace(self, nums, dist, cows):
        # Size of array
        n = len(nums)

        # Number of cows placed
        cntCows = 1

        # Position of last placed cow
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= dist:
                # Place next cow
                cntCows += 1

                # Update the last location
                last = nums[i]
            if cntCows >= cows:
                return True

        return False

    def aggressiveCows(self, nums, k):
        n = len(nums)
        nums.sort()
        low = 1
        high = nums[n - 1] - nums[0]
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high

