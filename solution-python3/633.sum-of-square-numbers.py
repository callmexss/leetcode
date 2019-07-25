class Solution:
    def judgeSquareSum(self, c):
        a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False
            

if __name__ == '__main__':
    solution = Solution()
    for i in range(10):
        print(i, solution.judgeSquareSum(i))

