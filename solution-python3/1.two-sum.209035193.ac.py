class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        hash_table = {}
        for i in range(len(nums)):
            current = nums[i]
            temp = target - current
            if temp in hash_table:
                return [i, hash_table[temp]] if i < hash_table[temp] else [hash_table[temp], i]
            else:
                hash_table[nums[i]] = i
                
        
