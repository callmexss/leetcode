#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.19%)
# Total Accepted:    629.2K
# Total Submissions: 2.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        reversed = 0

        while x:
            reversed = reversed * 10 + x % 10
            x = x // 10

        if reversed > 2 ** 31 - 1:  # one bit for sign
            return 0

        return -reversed if negative else reversed

