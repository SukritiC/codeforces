class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        count = 0
        hash_map = {0: 1}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]

            rem = prefix_sum - k

            count += hash_map.get(rem, 0)

            hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1

        return count
