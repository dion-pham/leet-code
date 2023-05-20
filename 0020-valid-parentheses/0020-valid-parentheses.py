class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {
            '[': ']',
            '{' : '}',
            '(' : ')'
        }
  
        for char in s: 
            if char in brackets: 
                stack.append(brackets[char])
            else: 
                if stack and char == stack[-1]:
                    stack.pop()
                else: 
                    return False
      
        return len(stack) == 0