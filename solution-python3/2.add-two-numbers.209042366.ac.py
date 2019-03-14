# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode', c=0) -> 'ListNode':
        val = l1.val + l2.val + c
        c, val = divmod(val, 10)
        ret = ListNode(val)
        
        if l1.next or l2.next or c:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret
