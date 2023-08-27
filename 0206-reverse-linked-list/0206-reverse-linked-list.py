# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #3 pointers: prev, current, next
        
        #   1  ->  2  ->  3  ->  4  ->  5
#prev <- current <-next
        #  prev  current next
    
    
        prev = None
        current = head
        
        
        while current: 
            next = current.next
            current.next = prev
            prev = current 
            current = next
            
        return prev 
        
    