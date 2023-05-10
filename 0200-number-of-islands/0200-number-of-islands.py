class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        #recursion with DFS

# call recursion on a list of deltas that explore up, down, right, and to the side 


# need visited set
# need to check if the position is inbounds
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid,r,c,visited) == True: 
                #do something with this function
                    count+=1
        return count
    
    def explore(self,grid, r,c,visited):
#         check for if inbounds, check for if hit water 0, and then check if in visited

        r_inbounds = 0 <= r < len(grid)
        c_inbounds = 0 <= c < len(grid[0])
        
        if not r_inbounds or not c_inbounds: 
            return False
        
        if grid[r][c] == "0":
            return False
        
        pos = (r,c)
        if pos in visited: 
            return False
        
        visited.add(pos)
        self.explore(grid,r+1,c,visited)
        self.explore(grid,r-1,c,visited)
        self.explore(grid,r,c+1,visited)
        self.explore(grid,r,c-1,visited)
        
        return True 