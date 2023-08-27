class Solution:
    def rob(self,nums):
        return self._rob(nums,0,{})
    def _rob(self, nums: List[int], i, memo) -> int:
        #start at the first index, take it
            #perform a recursive step that includes the first element
            #perform a recursive step that excludes the first element 
            
            
        # if len(nums) == 0: 
        #     return 0
        
        if i in memo:
            return memo[i]
        
        if i >= len(nums):
            return 0
        
        include = nums[i] + self._rob(nums, i+2,memo)
        exclude = self._rob(nums, i+1, memo)
        
        memo[i] = max(include, exclude)
        return memo[i]
        
        