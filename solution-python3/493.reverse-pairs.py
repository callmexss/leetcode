#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.pairs = 0
        def merge_sort(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            j = 0
            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                self.pairs += j
            
            return sorted(left + right)
        
        merge_sort(nums)
        return self.pairs

