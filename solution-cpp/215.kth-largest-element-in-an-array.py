import random


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        self.quick_sort(nums)
        print(nums)
        return nums[len(nums) - k]


    def quick_sort(self, nums):
        self.__quick_sort(nums, 0, len(nums) - 1)

    def __quick_sort(self, nums, l, r):
        if l >= r:
            return

        p = self.__partition(nums, l, r)
        self.__quick_sort(nums, l, p-1)
        self.__quick_sort(nums, p+1, r)

    def __partition(self, nums, l, r):
        loc = random.randint(l, r)
        print(l, r, loc)
        nums[loc], nums[r] = nums[r], nums[loc]
        pivot = nums[r]
        i = 0
        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    li = [1, 7, 3, 2, 4]
    Solution().quick_sort(li)
    print(li)

