'''
Find the repeating and missing number
Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

Note: You are not allowed to modify the original array.
'''

# optimal
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        result = []
        tSum = n*(n+1)//2
        cSum = 0
        c2Sum = 0
        t2Sum = 0
        for num in nums:
            cSum += num
            c2Sum = c2Sum + (num * num)

        for i in range (1, n+1):
            t2Sum = t2Sum + (i * i)

        delta1 = cSum - tSum
        delta2 = c2Sum  - t2Sum
        delta3 = delta2//delta1

        ans1 = (delta1 + delta3)//2

        result.append(ans1)
        ans2 = delta3 - ans1
        result.append(ans2)
        return result