class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

# sum cant be negative. if you start at a neg index, curSum is reset to 0
#continute iteration and update the curSum based on the bigger of curSum or maxSum 

        maxSum = nums[0]
        curSum = 0
        
        if len(nums) ==1:
            return nums[0]

        for num in nums: 
            
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum
    
    
    
    
    