class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bits = 1
        while bits <= n:
            if bits == n:
                return True
            bits = bits << 1
        return False

'''
# 解法二：
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
'''