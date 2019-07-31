class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        k = 0
        # [1, 2, 3, 1, 2, 3]
        # [2, 3, 4]
        while i < m and j < n:
            if nums1[m+i] < nums2[j]:
                nums1[k] = nums1[m+i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if j < n:
            print(j)
            nums1[m+j:] = nums2[j:]


def test(solution):
    li1 = [1, 3, 7, 8, 0, 0]
    li2 = [2, 3]
    solution.merge(li1, 4, li2, len(li2))
    print(li1)

    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    # bench_mark()

    print(~(-7))
    li = [1, 2, 3, 0, 0, 0]
    m = 3
    for i in range(m):
        li[m+i] = li[i]

    print(li)
    print(id(li))

    li[:2] = [0, 0]
    print(li)
    print(id(li))

    # for range[::-1]
    print(range(10)[::-1])
    for i in range(10)[::-1]:
        print(i, end=' ')
    print()

    # for range with ~i
    for i in range(10):
        print(~i, end=' ')
    print()

    # i ~i
    for i in range(10):
        print(i, ~i, bin(i), bin(~i % (1 << 8)))

    # a[:k] = b[i, i+k]
    a = [x for x in range(10)]
    b = [x ** 2 for x in range(5)]
    print(id(a), a)
    a[:5] = b[:5]
    print(id(a), a)
