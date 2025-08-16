class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        # while n >= 0:  # 当n==0时已经需要退出while循环，否则是一个死循环
        while n > 0:
            n = n // 5
            cnt += n
        return cnt