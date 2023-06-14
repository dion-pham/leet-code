class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#        height == height[i]
       # width == i
#     you need the difference in i between both to be large
#   and you can only take min(height[i], height[j]) for the height

# iterate through

        res = 0
        l, r = 0, len(height) -1
        while l < r: 
            area = (r-l) * min(height[l], height[r])
            res = max(res,area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1  
            else: 
                r -= 1
                
        return res
