class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#     dp: take or dont take first index
#     take every other index from that point on
#     return the max from either sum

        def _rob(self, nums, i,memo):
            if i in memo: 
                return memo[i]
            
            if i >= len(nums): return 0
            
            include = nums[i] + _rob(self,nums, i+2,memo)
            exclude = _rob(self,nums, i+1,memo)
           
            
            memo[i] = max(include, exclude)
            return memo[i]
        return _rob(self,nums,0,{})