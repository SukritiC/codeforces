def compute_max(l, r, n, k, count, cardpoint):
    if count == k:
        return 0

    sum_left  = cardpoint[l] + compute_max(l+1, r, n, k, count+1, cardpoint)
    sum_right = cardpoint[r] + compute_max(l, r-1, n, k, count+1, cardpoint)

    return max(sum_left, sum_right)



if __name__ == "__main__":
    cardpoint = [1,2,3,4,5,6,1]
    k=3

    l = 0
    n = len(cardpoint)
    r = n-1
    count = 0
    print(compute_max(l, r, n, k, count, cardpoint))




class Solution:
    def maxScore(self, cardScore, k):
        n = len(cardScore)
        lsum = rsum = 0
        max_sum = 0
        for i in range(k):
            lsum += cardScore[i]
        max_sum = lsum
        l1, r1 = 0, k - 1
        l2, r2 = n - 1, n - 1
        while r1 >= 0:
            lsum = lsum - cardScore[r1]
            r1 -= 1
            rsum += cardScore[l2]
            l2 -= 1
            max_sum = max(max_sum, (lsum + rsum))

        return max_sum



