class Solution:
    def maxProfit(self, prices):
        # buy low sell high
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        return maxProfit
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        '''
        The reason for updating the pointers that way on lines 8 and 9 is because if we were to update l += 1 and r += 1, we could potentially be doing repeated work cause ex:
        [6, 7, 3, 3, 6, 4]
        [[6, 7], 3, 3, 6, 4]
        profit = 1
        [[6, 7, 3], 3, 6, 4]
        profit = -3
        here, if we were to just incrament our left and right pointer by one then we would be get:
        [6, [7, 3, 3], 6, 4]
        profit = -4,
        by updating the pointers the way done on line 8 and 9, it makes it so that our profit will go to the next non negative profit.
        '''