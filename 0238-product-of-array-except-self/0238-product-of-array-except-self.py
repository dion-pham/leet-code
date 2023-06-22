class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
# On^2 == nested loops

# iterate one time, slice the nums list at the index, multiply by the remaining items after slice. 

        results = []
        temp = 1
        for num in nums:     
            results.append(temp)
            temp *= num 
            print(temp)
        
        temp2 = 1
        for i in range(len(nums) -1, -1,-1):
            results[i] *= temp2
            temp2 *= nums[i]
            
        return results
            
        
        # return
        