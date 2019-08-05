#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        # s[i-1] -> [0..n-1]
        for i in range(1, n + 1):
            # s[i-1] is valid char
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if i >= 2:
                # s[i-2:i] is valid char
                if 10 <= int(s[i-2:i]) <= 26:
                    dp[i] += dp[i-2]
                elif int(s[i-2:i]) == 0:  # s[i-2:i] is "00"
                    return 0

        return dp[-1]

