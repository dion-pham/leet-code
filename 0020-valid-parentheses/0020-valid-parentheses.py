class Solution:
    def isValid(self, s: str) -> bool:
        #stack data structure
        #use a hash map for every pair of opening to closing character
        
        #append all openers to the stack,
            #can add as many consecutive openers as you want PROVIDED that there are enough closers in the right                order
        stack = []
        closeToOpen = {')':'(', ']':'[','}':'{'}
        
        for char in s:
            if char in closeToOpen: 
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(char)
        if not stack: 
            return True
        else: 
            return False