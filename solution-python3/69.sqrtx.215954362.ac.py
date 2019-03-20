#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.80%)
# Total Accepted:    338.7K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        if x == 1:
            return 1

        left = 0
        right = x
        # mid = left + (right - left) // 2
        mid = (right + left) // 2


        while right - left > 1:
            if mid * mid == x:
                return mid

            if mid * mid > x:
                right = mid
            else:
                left = mid
            mid = (right + left) // 2

        return mid
        

