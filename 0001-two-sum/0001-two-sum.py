class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate through the array
        #{0:7, index: difference}
        #add the number at the index as a key, difference as a value
            #for next index, if target-index is equal to a key in hash, then you have your two return values 
            
        differenceHash = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in differenceHash: 
                return [i, differenceHash[nums[i]]]
            if difference not in differenceHash: 
                differenceHash[difference] = i

            
            
            
#    {7:0,}
#   {3:0, 4:1, }