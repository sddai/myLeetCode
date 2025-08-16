# 处理两个字符串，用双指针法
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n) # 先建立列表用于暂存中间结果并直到得到最终结果，技巧：去掉未使用的0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                multi = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                carry = (res[i + j + 1] + multi) // 10
                # multi = multi % 10
                res[i + j + 1] = (res[i + j + 1] + multi) % 10
                res[i + j] += carry    
                # 问题：如果num1和num2很长，carry可以是3位数或者更长吗？
                # 回答：只需要考虑每一轮循环北部的操作即可：
                # 每轮循环，res[i]中原有的数字为此前加上来的carry，carry最大是1，本轮加上去的时9*9%10=81%10=8，所以carry最大是9
        k = -1  # 要注意k的起点是-1
        print(res)
        for i in range(m + n):
            if res[i] == 0:
                k = i
                # continue
            else:
                break
        if k == m + n - 1: return "0"
        return "".join(str(x) for x in res[k+1:])
    
'''
       1 2 3
    x  4 5 6
    --------
         1 8
       1 2
     0 6     -> 123 x 6
    --------
       7 3 8
    --------
       1 5
     1 0
   0 5
   ---------
==============
       9 9 9
    x  9 1 9
    --------
         8 1
       8 1
     8 1
    --------
     9 9 9 1
    --------
       0 9
     0 9  
   0 9
   ---------
观察可以得出，res[i]在每一轮循环中，需要加上两个数：
1. 9*9=81，所以进位上来的最大是8
2. 当前位是两个数相乘的个位，最大是9
3. 所以每一轮产生的carry最大是1
4. res是滚动的，所以每一轮循环中都不会超过上限
'''
