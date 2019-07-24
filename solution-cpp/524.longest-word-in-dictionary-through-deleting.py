import heapq


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ret = []
        for word in d:
            it = iter(s)
            if all(x in it for x in word):
                ret.append(word)

        if not ret:
            return ''
        else:
            ret.sort(key=lambda x: (-len(x), x), reverse=True)
            return ret.pop()


class Solution1:
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return max(sorted(filter(isSubsequence, d)) + [''], key=len)


class Solution2:
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return min(filter(isSubsequence, d) + [''], key=lambda x: (-len(x), x))


class Solution3:
    def findLongestWord(self, s, d):
        best = ''
        for x in d:
            if (-len(x), x) < (-len(best), best):
                it = iter(s)
                if all(c in it for c in x):
                    best = x
        return best


class Solution4:
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        d.sort(key=lambda x: (-len(x), x))
        return next(itertools.ifilter(isSubsequence, d), '')


class Solution5:
    def findLongestWord(self, s, d):
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''


class Solution6:
    def findLongestWord(self, s, d):
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            word = heapq.heappop(heap)[1]
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ''


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

    s = "abpcplea"
    t = 'apple'
    it = iter(s)
    print(all(x in it for x in t))

    d = ["ale","apple","monkey","plea", "moondy"]
    d = ['a', 'b', 'c']
    # This sort manner is worth learning
    # COMPARE BY LENGTH AND LEXICOGRAPHICAL
    d.sort(key=lambda x: (-len(x), x), reverse=True)
    print(d)

    print('a' < 'b')  # True

    li = [1, 7, 3, 2, 4]
    heap = heapq.heapify(li)
    while li:
        print(heapq.heappop(li))

