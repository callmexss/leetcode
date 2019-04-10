class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)  # use a collections.deque() is also fine.
        l, r = 0, len(A) - 1

        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                res[r - l] = left * left
                l += 1
            else:
                res[r - l] = right * right
                r -= 1

        return res
