# 用单调栈
# 原理：从左向右扫描，遇到一个数字，如果下一个数字比当前值大，那么保留当前数字（小的那个）会使得总数值更小
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        cut = n - k
        for c in num:
            while stack and stack[-1] > c:
                if k == 0:
                    break
                stack.pop()
                k -= 1
            stack.append(c)
        res = "".join(stack[:cut]).lstrip("0")   # 注意，这时候就不可以再使用k截断字符串了，因为k可能已经递减为0
        return res if res else "0"
