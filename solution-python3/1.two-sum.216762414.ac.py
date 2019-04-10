class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, num in enumerate(nums):
            # find one!
            if target - num in hash_table:
                return [hash_table[target - num], i]
            # record current number and its index
            hash_table[num] = i

        # empty list
        return []
        
