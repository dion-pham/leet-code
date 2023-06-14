class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
#perform a dfs starting at 0,0
# want to keep track if starting position can end up at both pacific and atlantic ocean
# if it can, append it to a list that will be return
# keep track of visited to see what you have already visited 
# conditional: if r,c in visited but has true for pacific, see if it works for atlantic?

# perform dfs on every position that borders the pacific ocean
# perform dfs on every position that borders the atlantic ocean
# keep track of visited for both
    # since you are traveling from the outside in, your only requirement for dfs
    # is that the next position has to have a greater water count than the one
    #that came before it     
# if there is overlap between the visited, append them to a new list

        rows, column = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(self,r,c,visited,prevHeight):
            if (r < 0 or c < 0 or (r,c) in visited or
               r == rows or c == column or heights[r][c] < prevHeight
               ):
                return
            visited.add((r,c))
            dfs(self,r+1,c,visited,heights[r][c])
            dfs(self,r-1,c,visited,heights[r][c])
            dfs(self,r,c+1,visited,heights[r][c])
            dfs(self,r,c-1,visited,heights[r][c])
            
            

        for c in range(column):
            dfs(self,0, c, pac, heights[0][c])
            dfs(self,rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(self,r, 0, pac, heights[r][0])
            dfs(self,r, column -1, atl, heights[r][column-1])
            
        res = []
        for r in range(rows):
            for c in range(column):
                if (r,c) in pac and (r,c) in atl: 
                    res.append((r,c))
                    
        return res
        
    
    
    