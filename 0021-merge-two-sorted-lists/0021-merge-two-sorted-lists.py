# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
# given two heads of sorted LL == give two pointers at the head of each, to which you can move then to progress in LL
# make a dummy head
# append one start of LL to the dummy head, then go in alternating order depending on which LL is shorter from that point on
# if one LL is empty, append the rest of the other LL 

        dummyHead = ListNode()
        tail = dummyHead
        
        while list1 and list2: 
            if list1.val < list2.val: 
                tail.next = list1
                list1 = list1.next 
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if not list1: 
            tail.next = list2
        if not list2: 
            tail.next = list1
            
        return dummyHead.next
        