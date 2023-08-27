class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #iterate through  the array
        
        
        #max sum 
        
        
        #temp sum 
        
        #if the temp sum < 0, reset it back to zero 
        #keep reupdating max sum if its non negative and finish the iteration
        if len(nums) ==1:
            return nums[0]
        
        maxSum = nums[0]
        tempSum = 0
        for num in nums: 
            if tempSum < 0: 
                tempSum = 0
            tempSum += num
            maxSum = max(maxSum, tempSum)
        return maxSum 
            
            