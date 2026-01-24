class Solution:
    def findMin(self, arr):
        low = 0
        high = len(arr) - 1
        min_val = 1e9
        while low <= high:
            mid = (low + high) // 2

            if arr[low] <= arr[mid]:
                min_val = min(min_val, arr[low])
                low = mid + 1
            else:
                min_val = min(min_val, arr[mid])
                high = mid - 1
        return min_val