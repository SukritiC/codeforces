# Brute Force Solution
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])

        return ans
'''
 TC - O(2N)
 SC - O(2N)
'''

# Better Solution
'''
Here instead of maintaining the right array, we compute the right & max amoung left right during the iteration
TC - O(2N)
SC - O(N)
'''

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        left = [1] * n
        curr = 1
        right = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        sum_val = max(1, left[n - 1])
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr = right + 1
            else:
                curr = 1
            right = curr
            sum_val += max(left[i], curr)

        return sum_val