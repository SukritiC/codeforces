"""
Optimal Apprach
Two Pointer Solution
keep increasing the right pointer uptll the value of sum <= k, once the sum increases k , start trimming the subarray
from left
if sum == k right -left is the length,

This solution will be ineffective if there are negative elements in the array
"""


class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        maxLength = 0
        l = r = 0
        sum_val = nums[0]
        while r < n:

            while l <= r and sum_val > k:
                sum_val -= nums[l]
                l += 1

            if sum_val == k:
                maxLength = max(maxLength, r - l + 1)

            r += 1
            if r < n:
                sum_val += nums[r]

        return maxLength


""" 
Better Approach
Hashing Solution - O(N) Time and Space

Approach  - Hashing the prefix sum of all array elements upt index i, if prefix sum is same as k - update the maxLength,
For finding subarray upto index i with sum k, there should exist a prefix sum -k subarray also. 
therefore checking for prefix sum -k subarray in hashmap, if there is, update the maxLength, 
if the prefix sum isn't already in hashmap update it 

This solution is effective even when there are negative elements in the array
"""
class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        maxLength = 0
        hash_map = {}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == k:
                maxLength = max(maxLength, i + 1)
            rem = prefix_sum - k

            if rem in hash_map:
                maxLength = max(maxLength, i - hash_map[rem])
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i

        return maxLength


