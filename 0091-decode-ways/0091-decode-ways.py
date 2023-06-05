class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#   use the indeces from the alphabet
#   find all possible combinations of the string that could create the number
#   use dynamic programming
#   12 = how many ways to form 1 + 2 and how many ways to form 12 


        dp = { len(s): 1 }
    
        def dfs(self, i):
            if i in dp:
                return dp[i]
            
            if s[i] == '0': return 0
            
            res = dfs(self, i+1)
            if (i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')):
                res += dfs(self,i+2)
            
            dp[i] = res
            return res
        
        return dfs(self, 0)