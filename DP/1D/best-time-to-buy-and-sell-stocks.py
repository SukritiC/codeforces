class Solution:
    '''
    To buy and sell stocks only once
    '''
    def stockBuySell(self, arr, n):
        maxProfit = 0
        mini = arr[0]
        for i in range(1,n):
            currProfit = arr[i] - mini
            maxProfit = max(maxProfit, currProfit)
            mini = min(mini, arr[i])
        return maxProfit
