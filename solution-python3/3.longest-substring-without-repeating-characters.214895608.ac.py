#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.03%)
# Total Accepted:    831.4K
# Total Submissions: 3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        longest = 0

        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                # repeating words show in s[start: i],
                # so update start
                start = last_seen[c] + 1  
            else:
                # c is not in last_seen or c is ahead of start,
                # which means from start to i there is no repeating characters
                longest = max(longest, i - start + 1)
            last_seen[c] = i

        return longest


