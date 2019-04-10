#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (76.43%)
# Total Accepted:    91.2K
# Total Submissions: 119.4K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#
class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
        

