class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
# two pointers: left and right
# have a max start at 0 and be replaced by the greatest difference as you progress
#left = lowest number
# right will be the number that you subtract lowest from to keep a track of max
        res = 0
        left = prices[0]
        for price in prices: 
            if price < left: 
                left = price
            res = max(res, price-left )
        return res