# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
#         set two pointers, one at head of list 1 and one at head of list 2
        
        dummy_head = ListNode(None)
#       setting tail to first point to dummy_head so that you can append new node
#       values through tail.next
        tail = dummy_head
        current_1 = list1
        current_2 = list2
        
        while current_1 and current_2: 
            if current_1.val < current_2.val: 
                tail.next = current_1 
                current_1 = current_1.next
            else: 
                tail.next = current_2
                current_2 = current_2.next 
            tail = tail.next
                
        if current_1: tail.next = current_1
        if current_2: tail.next = current_2
            
        return dummy_head.next 