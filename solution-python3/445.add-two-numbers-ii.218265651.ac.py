#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (49.44%)
# Total Accepted:    83.9K
# Total Submissions: 169.4K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def calcu_len(head: ListNode) -> int:
    i = 0
    while head:
        i += 1
        head = head.next
    return i

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = l1
        num1 = 0
        while node:
            num1 = num1 * 10 + node.val 
            node = node.next

        node = l2
        num2 = 0
        while node:
            num2 = num2 * 10 + node.val
            node = node.next

        total = num1 + num2

        if not total:
            return ListNode(total)

        res = None

        while total:
            total, digit = divmod(total, 10)
            new_node = ListNode(digit)
            new_node.next = res
            res = new_node

        return res
        

