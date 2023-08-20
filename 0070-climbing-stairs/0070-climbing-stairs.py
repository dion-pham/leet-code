class Solution(object):
    def climbStairs(self,n):
        return self._climbStairs(n,{})
    def _climbStairs(self, n, memo):
        """
        :type n: int
        :rtype: int
        """
        
        #memoization: to allow for faster complexity 
        
        #put changing value in memo
        if n in memo: 
            return memo[n]
        
        #given a total. see how many steps if takes to get to the end
        #recursion - each recursive step, you are subtracting either 1 or 2 from n
        #base case: when n = 0, return 1 to bubble back up to the top of the call stack. indicating 1 valid way
        
        if n == 0: 
            return 1
        if n < 0: 
            return 0
        
        memo[n] = self._climbStairs( n-1, memo) + self._climbStairs( n-2, memo)
        return memo[n]