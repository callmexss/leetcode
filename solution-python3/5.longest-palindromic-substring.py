#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


class Solution:
    max_len = 0
    loc = 0

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        for i in range(length):
            self.extend_palindrome(s, i, i)
            self.extend_palindrome(s, i, i+1)

        return s[self.loc: self.loc + self.max_len]

    def extend_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.max_len < k - j - 1:
            self.loc = j + 1
            self.max_len = k - j - 1

