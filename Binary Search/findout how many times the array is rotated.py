class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        min_val = 1e9
        index = -1
        while low <= high:
            mid = (low + high) // 2

            #if arr is not pivoted
            if arr[low] <= arr[high]:
                if arr[low] < min_val:
                    index = low
                    min_val = arr[low]
                break

            if arr[low] <= arr[mid]:
                if arr[low] < min_val:
                    min_val = arr[low]
                    index = low
                low = mid + 1
            else:
                if arr[mid] < min_val:
                    min_val = arr[mid]
                    index = mid
                high = mid - 1
        return index