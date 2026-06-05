"""
Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Brute Fore Solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prod = 1
        res = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if(j == i):
                    continue
                prod *= nums[j]
            res.append(prod)
        return res


# Optimal Solution

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prod = 1
        res = []
        n = len(nums)
        flag = []
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                flag.append(i)
        print(len(flag))
        for i in range(n):
            if len(flag) > 1:
                res.append(0)
            elif len(flag) > 0:
                if i in flag:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // nums[i])
        return res
