# 两种套路：1. 贪心greedy；2. 栈stack -> 栈方法内存超限
# 贪心：count计数未匹配到的左括号，count<0说明有未匹配的右括号
# 遇到左括号：count += 1
# 遇到连续两个右括号：count -= 1
# 只遇到一个右括号：只有一个右括号无法跟其他括号匹配，必须加上一个右括号，再匹配一个左括号（也就是count -= 1）

# 方法二：计数法
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        count_left = 0
        i = 0
        res = 0
        while i < n:
            c = s[i]
            if c == "(":
                count_left += 1
            if c == ")":
                if i + 1 < n and s[i + 1] == ")":
                    count_left -= 1
                    i += 1
                else:
                    # if i + 1 >= n:
                    #     res += 2
                    res += 1   # 人为加一个左括号
                    count_left -= 1  # 然后销掉一个左括号
            if count_left < 0:  # 缺左括号，加一个
                count_left = 0
                res += 1
            i += 1
        return res + count_left * 2 

'''
# 方法一：栈（得分更高）
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        stack = []
        # p = 0
        res = 0
        i = 0
        while i < n:
            c = s[i]
            if c == "(":
                stack.append(c)
            elif c == ")":
                i += 1
                if i >= n:
                    if stack:
                        stack.pop()
                        res += 1
                    else:
                        res += 2
                    # res += 1
                    # if stack: stack.pop()
                    # else: res += 2
                    continue
                c2 = s[i]
                if stack and c2 == ")":
                    stack.pop()
                elif stack and c2 == "(":
                    # stack.pop()
                    # stack.append(c2) # 这两句相当于栈中元素没变，可以省略
                    res += 1
                elif not stack and c2 == ")":
                    res += 1   # 两个res可以进一步整合
                elif not stack and c2 == "(":
                    res += 2
                    stack.append(c2)
                # else:
                #     res += 1
            i += 1
        if stack:
            return 2 * len(stack) + res
        return res
'''