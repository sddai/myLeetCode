# 总结：
# 1. sign，num里边存储的实际上是上一轮循环的结果，遇到运算符或者遇到结尾，就把上一轮的结果入栈
# 2. 注意string.strip()只能去掉首尾的空格，无法去掉中间的空白字符。
# 3. 【引申】关于括号：
#     无论多少层括号嵌套，通过 calculate 函数递归调用自己，都可以将括号中的算式化简成一个数字。
#     换句话说，括号包含的算式，我们直接视为一个数字就行了。
# 4. 递归的开始条件和结束条件是什么？
#     遇到 "(" 开始递归，遇到 ")" 结束递归

# from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        def calc(s):
            # i = 0
            num = 0
            sign = "+"
            stack = []
            # print(s)
            n = len(s)
            # for c in s:
            for i in range(n):
                c = s[i]
                # print("c: ", c)
                # c = s[i]
                if c.isdigit():
                    num = num * 10 + (ord(c) - ord("0"))
                    # num = num * sign # 处理每一位，处理过后统一加符号
                    # stack.append(num)
                # else:   # 
                if (not c.isdigit() and c != " ") or i == n - 1:  # 此时遇到了一个新的运算符号，说明前边的数字已经处理完成并保存在了num里边，应该将这个数字和上一个保存下来的运算符sign进行运算，加减就入栈，乘除就与栈顶元素进行计算并替代栈顶元素
                    # pre = 0 # 初始化 pre 以解决当符号是 + 或 - 时出现 UnboundLocalError 的问题
                    # if c == "+":    # 出错的原因：switch的条件写错了，switch的条件应该是sign（或者命名为preSign更清晰）
                    if sign == "+":
                        # num = num  # 这里处理错了，num最后保存了sign中的"+"
                        stack.append(num)
                        # sign = "+"
                    # elif c == "-":
                    elif sign == "-":
                        # num =  num * (-1)
                        stack.append(-num)
                        # sign = "-"
                    elif sign == "*":
                        stack[-1] = stack[-1] * num 
                        # 例如3+2*2：
                        # 扫描到*的时候，stack里边是[3,2]
                    # elif c == "/":
                    elif sign == "/":
                        # print(stack)
                        # print(s)
                        # stack[-1] = stack[-1] // num
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
            # print(stack)
            return sum(stack)
        # print(s)
        # s = s.strip()   # 【易错！】strip只去掉了字符串开头和结尾处的空白字符，但是保留了中间的空格
        res = calc(s)
        return res

    # 解法二：
    # from collections import deque
    # def calculate(self, s: str) -> int:
        
    #     def helper(s: List) -> int:
    #         stack = []
    #         sign = '+'
    #         num = 0

    #         while len(s) > 0:
    #             c = s.popleft()
    #             if c.isdigit():
    #                 num = 10 * num + int(c)

    #             if (not c.isdigit() and c != ' ') or len(s) == 0:
    #                 if sign == '+':
    #                     stack.append(num)
    #                 elif sign == '-':
    #                     stack.append(-num)
    #                 elif sign == '*':
    #                     stack[-1] = stack[-1] * num
    #                 elif sign == '/':
    #                     # python 除法向 0 取整的写法
    #                     stack[-1] = int(stack[-1] / float(num))                    
    #                 num = 0
    #                 sign = c

    #         return sum(stack)
    # # 需要把字符串转成列表方便操作
    #     return helper(deque(s))