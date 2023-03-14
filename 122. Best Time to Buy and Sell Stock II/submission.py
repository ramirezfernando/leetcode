class Solution:
    def maxProfit(self, prices):

        currProfit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                currProfit += prices[i + 1] - prices[i]
        return currProfit
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''