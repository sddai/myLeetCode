class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            n = n & (n - 1)
            ans += 1
        return ans
'''
# 法二：循环检查法
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i)) 
        return ret
'''