class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for i, p in enumerate(S):
            if p == '(':
                if not stack:
                    stack.append(p)
                else:
                    stack.append(p)
                
            elif p == ')':
                if not stack:
                    count += 1
                else:
                    stack.pop()
                    
        return len(stack) + count
