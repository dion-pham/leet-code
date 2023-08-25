class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp problem
        #base case: when you get to the bottom right corner
            #return 1 indicating that that was one unique path
        
        def dfs(row,col, memo):
            
            pos = (row,col)
            if pos in memo:
                return memo[pos]
            
            if row == m-1 and col == n-1: 
                memo[pos] =1
                return memo[pos]            
            #check if in bounds
            if row == m or col == n: 
                memo[pos] = 0
                return memo[pos]  
            
            down = dfs(row+1,col,memo)
            right = dfs(row,col+1,memo)
            
            memo[pos] = down +right
            return memo[pos]  
        
        return dfs(0,0, {})
            
            
        