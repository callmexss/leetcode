#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.86%)
# Total Accepted:    293.1K
# Total Submissions: 949.3K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:  # boundary condition
            return s

        zigzag = [[] for _ in range(numRows)]
        direction = -1  # for up direction
        row = 0

        for c in s:
            zigzag[row].append(c)

            if row == 0 or row == numRows - 1:
                direction = -direction  # change direction

            row += direction

        return ''.join(map(''.join, zigzag))


