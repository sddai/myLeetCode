# 简单题，一次通过
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        m = len(s)
        n = len(t)
        while i <= m - 1 and j <= n - 1:
            c1 = s[i]
            c2 = t[j]
            if c1 == c2:
                i += 1
                j += 1
            else:
                j += 1
        if i == m:
            return True
        else:
            return False