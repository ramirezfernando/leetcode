class Solution:
    def coinChange(self, coins, amount):

        @lru_cache(None)
        def dfs(currChange):
            
            if currChange == 0:
                return 0
            if currChange < 0:
                return float('inf')
            
            minDepth = float('inf')
            for coin in coins:
                depth = 1 + dfs(currChange - coin)
                minDepth = min(minDepth, depth)
            return minDepth


        minCoins = dfs(amount)
        if minCoins == float('inf'):
            return -1
        return minCoins