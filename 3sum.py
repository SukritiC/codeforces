'''
3 Sum

Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.
'''

# Better Solution
from typing import List

class Solution:
    # Function to find triplets having sum equals to 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n):
            # Set to store elements seen so far in the loop
            hashset = set()

            for j in range(i + 1, n):
                # Calculate the 3rd element needed to reach target
                third =  - (nums[i] + nums[j])

                """ Find if third element exists in
                 hashset (complements seen so far)"""
                if third in hashset:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], third]

                    """ Sort the triplet to ensure
                    uniqueness when storing in set"""
                    temp.sort()
                    triplet_set.add(tuple(temp))

                """ Insert the current element 
                into hashset for future checks"""
                hashset.add(nums[j])

        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        #Return the ans
        return ans

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.threeSum(nums)

    # Print the result
    for triplet in ans:
        print(f"[{', '.join(map(str, triplet))}]")


# Optimal Solution

class Solution:
    def threeSum(self, nums):
        result =[]
        nums.sort()
        n = len(nums)
        if n < 3:
            return result
        for i in range(n):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val < 0:
                    j += 1
                elif val > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return result
