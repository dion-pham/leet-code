class Solution(object):
    def climbStairs(self,n):
        return self._climbStairs(n, {})

    def _climbStairs(self, n,memo):
        """
        :type n: int
        :rtype: int
        """

#  recursion, take 1 step or take two steps
#  base case: if n== 0, return the number of steps
        if n in memo: 
            return memo[n]

        if n < 0:
            return 0
        if n == 0: 
            return 1
        
        memo[n] = self._climbStairs(n-1,memo) + self._climbStairs(n-2,memo)
        return memo[n]