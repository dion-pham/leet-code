class Solution(object):
    def coinChange(self, coins, amount):
        if self._coinChange(coins, amount,{}) == float('inf'):
            return -1
        else: 
            return self._coinChange(coins, amount, {})
    
    def _coinChange(self, coins, amount, memo):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
#      recursion: amount - coin
#      base case: if amount == 0, return 0
#           w each recursive step, return 1 
        
        if amount in memo: 
            return memo[amount]

        if amount == 0: 
            return 0
        
        if amount < 0: 
            return float("inf")
#         return infinity because if you return -1 here, you are return an invalid answer with 1 subtracted from it
        
        min_coins = float("inf")
        
        for coin in coins: 
            num_coins  = 1 + self._coinChange(coins, amount - coin, memo)
            if num_coins < min_coins: 
                min_coins = num_coins
        
            
        memo[amount] = min_coins
        return memo[amount]
        
       