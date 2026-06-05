'''
Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, there is only one repeated number in nums (but can repeated more than once), return this duplicate number.
You must not modify the array (assume it is read-only), and you must use only constant extra space.
Your algorithm should run in less than O(n²) time.
'''

# Brute force approach

class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        vals = []
        for num in nums:
            if num in vals:
                return num
            vals.append(num)
        return -1

# Better Approach

class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        nums.sort()
        vals = nums[0]
        for i in range(1,n):
            if nums[i] == vals:
                return nums[i]
            vals = nums[i]
        return -1

# Optimized Approach

class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # First phase: find intersection inside the cycle
        while True:
            # Move slow pointer by one step
            slow = nums[slow]
            # Move fast pointer by two steps
            fast = nums[nums[fast]]
            # Break if pointers meet
            if slow == fast:
                break

        # Second phase: find entry point of the cycle
        # Reset fast pointer to start
        fast = nums[0]
        # Move both pointers one step at a time until they meet
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return duplicate number
        return slow