class Solution:
    def eraseOverlapIntervals(self, intervals):
        end = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= end:
                end = i.end
            else:
                erased += 1
        return erased

def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()
    ret = Solution().eraseOverlapIntervals([[1, 2], [1, 2]])
    print(ret)
