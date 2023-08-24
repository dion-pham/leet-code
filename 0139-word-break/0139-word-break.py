class Solution:
    def wordBreak(self,s,wordDict):
        return self._wordBreak(s,wordDict,{})
    def _wordBreak(self, s: str, wordDict: List[str], memo) -> bool:
        
        #iterate through the wordDict
        #dp problem: choose a word and build your 
            #decision/recursion tree off of that
        #choose first word: 
            #if word present in string
                #slice the string and perform a recursive step on the new string segment
                #if s length eventually becomes 0, return 0
        if s in memo: 
            return memo[s]
        
        if len(s) == 0: 
            memo[s] = True
            return memo[s]

                
        print(s,'step')
        for word in wordDict: 
            if s.startswith(word): 
                #slice string up until that word
                if self._wordBreak(s[len(word):], wordDict, memo):
                    memo[s] = True
                    return memo[s]
                               
                               
        memo[s] = False
        return memo[s]
                               
        