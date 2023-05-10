class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        hash = {}
        for index, num in enumerate(nums):
            # print(index,num)
            difference = target - num
            if difference not in hash: 
                hash[num] = index 
            else: 
                return [hash[difference], index]
            
        return 
    
# iterate through, target minus the index. we will get the difference == 7 for the index of 0
#  {7: 0 , 2: 1}