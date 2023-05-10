# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        if head is None: 
            return None
        
        current = head 
        while current:
#           switch arrows first 
            next = current.next
            current.next = prev
        
#           switch pointers
            prev = current
            current = next 
            
            
        return prev
            
            
#             prev -> current -> next 