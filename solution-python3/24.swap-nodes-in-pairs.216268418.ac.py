#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.53%)
# Total Accepted:    289.5K
# Total Submissions: 665.1K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # two pointers

        # is head none or list.size < 2?
        if not head or not head.next:
            return head

        # more general condition?
        slow = head
        fast = head.next

        while slow and fast:
            # exchange two values
            slow.val, fast.val = fast.val, slow.val

            # move pointers
            try:
                slow = fast.next
                fast = slow.next
            except:  # to the end
                break

        return head






        

