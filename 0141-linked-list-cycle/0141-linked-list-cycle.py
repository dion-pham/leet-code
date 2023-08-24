# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #iterate through the LL
        #add each note to the set
        #the tail's next pointer (pos) should be null at some point
        #if the tail instead points to a value thats already in the set, then return false
        #return true if otherwise
        
        current = head
        visited = set()
        
        while current: 
            if current in visited: 
                return True
            visited.add(current)
            current = current.next
        return False
    
    
#       current = head
#   set_check = set()
  
#   while current: 
#     if current in set_check:
#       return True
#     set_check.add(current)
#     current = current.next
#   return False
