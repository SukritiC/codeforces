'''
Brute Force approach
TC - O(n^3)
'''

class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                xor_val = 0
                for l in range(i, j+1):
                    xor_val ^= nums[l]
                if xor_val == k:
                    count +=1
        return count


"""
Optimal Approach - by using hashing 
Similar to counting subarray with sum = k, here we're counting subarrays with xor k
we'er keeping a hashmap of prefix xor values,

as for sum = k question, we were searching for x-k prefix sum in the hashmap and using its corresponding counts 
similarly here - in an array of xor XR, for each subarray of xor k there will exist a other half of xor XR^k
 

"""


class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        count = 0
        xorr = 0
        hash_map = {}
        hash_map[xorr] = hash_map.get(xorr, 0) + 1

        for i in range(n):
            xorr ^= nums[i]
            rem = xorr ^ k
            count += hash_map.get(rem, 0)
            hash_map[xorr] = hash_map.get(xorr, 0) + 1

        return count
