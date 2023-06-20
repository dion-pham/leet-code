class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

#   two pointers: left and right
#   area: length * height
#   length == difference in i between your left/right pointers
#   height == min(height[left], height[right])
#   max variable for area
#   move left or right pointer according to: which is the lower between the two 

        left, right = 0, len(height) - 1
        area = 0

        while left != right: 
            tempArea = (right - left) * min(height[left], height[right])
            if tempArea > area: 
                area = tempArea

            if height[left] < height[right]: 
                left += 1 
            else: 
                right -= 1


        return area 