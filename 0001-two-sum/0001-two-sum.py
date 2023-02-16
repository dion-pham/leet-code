class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # given a list, find indexes of two numbers that equal the target
        # iterate through list, start by comparing the first index and its sums
            # to that of the other numbers
        # new_list = []
        hash_map = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[n] = i
        return
