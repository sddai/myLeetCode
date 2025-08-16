class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        stack = []
        res = 0
        for i in range(n):
            if s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    res += 1
            else:
                stack.append("(")
        if not stack:
            return res
        for c in stack:
            res += 1
        return res