class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            dp[i] = dp[i-1] and nums[i-1] >= nums[i]

        return dp[-1]
