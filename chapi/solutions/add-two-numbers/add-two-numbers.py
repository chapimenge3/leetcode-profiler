# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        starter = None
        prev = None
        carry = 0
        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0 
            res_num = val_1 + val_2 + carry
            if res_num > 9:
                carry = 1
                res_num = res_num % 10
            else:
                carry = 0
            res_node = ListNode(val=res_num)
            if prev:
                prev.next = res_node
            
            prev = res_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not starter:
                starter = res_node
        
        if carry:
            node = ListNode(val=carry)
            prev.next = node

            
        return starter
