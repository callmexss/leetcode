class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # can only delete one char, so we can pass once
                return s[l: r] == s[l: r][::-1] or s[l+1: r+1] == s[l+1: r+1][::-1]
            l += 1
            r -= 1
        return True


class Solution1:
    def validPalindrome(self, s: str) -> bool:
        # Check if it is palindrome.
        if s == s[::-1]:
            return True
        # Check every "palindromness" for every possible one character difference.
        for i in range(len(s) - 1):
            if s[i] != s[~i]:
                return s[i: ~i - 1] == s[i + 1: ~i][::-1] or s[i + 1: ~i] == s[i + 2: len(s) - i][::-1]
        return False    



if __name__ == '__main__':
    solution = Solution()
    solution1 = Solution1()
    long_str = ''
    solution.validPalindrome('')
    solution1.validPalindrome('')

    for i in range(10):
        print(i, ~i)
        assert ~i == -(i+1)

