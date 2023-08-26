class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #left,right pointers
        #calculate max area, update as you move pointers inwards
        #which ever pointer is smaller, move that one in 
        #when pointers meet, return the max area that you found
        
        
        left, right = 0, len(height) - 1
        maxArea = 0
        
        while left<right: 
            tempLength= min(height[left], height[right])
            # print(tempLength)
            maxArea = max(maxArea, (tempLength*(right-left)))
            print(maxArea)
            if height[right]>height[left]: 
                left += 1
            else: 
                right -= 1
                
        return maxArea