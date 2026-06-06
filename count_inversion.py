'''

Count Inversions
Given an integer array nums. Return the number of inversions in the array.

Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

It indicates how close an array is to being sorted.

A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.
'''
class Solution:
    def merge(self, arr, low, mid, high):

        # Temporary array for merging
        temp = []

        # Starting indices of left and right halves
        left = low
        right = mid + 1

        # Count variable to count the pairs
        cnt = 0

        # Merge sorted halves into temp array
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:

                temp.append(arr[left])
                left += 1

            else:
                temp.append(arr[right])

                # Count inversions
                cnt += (mid - left + 1)

                right += 1

        # Copy remaining elements of left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Copy remaining elements of right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy elements from temp
        # array back to original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        # Return the count of inversions
        return cnt

    # Merge sort function to recursively sort and count inversions
    def mergeSort(self, arr, low, high):
        cnt = 0
        if low < high:
            mid = low + (high - low) // 2

            # Sort left half
            cnt += self.mergeSort(arr, low, mid)

            # Sort right half
            cnt += self.mergeSort(arr, mid + 1, high)

            # Merge and count inversions
            cnt += self.merge(arr, low, mid, high)
        return cnt

    # Function to find number of inversions in an array
    def numberOfInversions(self, nums):

        # Size of the array
        n = len(nums)

        # Count the number of pairs
        return self.mergeSort(nums, 0, n - 1)