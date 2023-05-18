class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
#       robot starts at grid[0][0]
#       base case returns as 1 added to unique path when it reached bottom right corner
#       BRC is denoted at when grid[m-1][n-1]

# maybe explore a helper function to see if you reach BRC by going either down or right
        return self._uniquePaths(m,n,{})
    def _uniquePaths(self, m,n,memo):
        pos = (m,n)
        if pos in memo: 
            return memo[pos]
        
        if m == 0 or n == 0:
            return 0 
    
        if m == 1 and n == 1: 
            return 1
        
        down = self._uniquePaths(m-1 , n, memo)
        right = self._uniquePaths(m, n-1, memo)
        
        memo[pos] = down + right
        return memo[pos]
        
        