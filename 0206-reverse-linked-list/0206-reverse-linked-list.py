# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #3 pointers. prev, current, next
        
        prev, current = None, head
        while current: 
            #keep track of next variable so you dont lose it when you break off the current.next connection
            next = current.next 
            current.next = prev
            prev = current 
            current = next
        return prev