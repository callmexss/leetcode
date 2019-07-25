class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        li = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            # while li[l] not in vowels:
            #     l += 1
            # this will raise list index out of range exception
            # when all of the chars not in vowels
            # for example ',.'
            while l < r and li[l] not in vowels:
                l += 1
            while l < r and li[r] not in vowels:
                r -= 1
            if l > r:
                break
            li[l], li[r] = li[r], li[l]
            l += 1
            r -= 1

        return ''.join(li)


if __name__ == '__main__':
    solution = Solution()
    ret = solution.reverseVowels('bcd')
    print(ret)
