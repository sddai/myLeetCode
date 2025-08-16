
def calculate(s: str) -> int:
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
            print("c: ", c)
            # c = s[i]
            if c.isdigit():
                num = num * 10 + (ord(c) - ord("0"))
                # num = num * sign # 处理每一位，处理过后统一加符号
                # stack.append(num)
            # else:   # 
            if not c.isdigit() or i == n - 1:
                # if c == "+":    # 出错的原因：switch的条件写错了，switch的条件应该是sign（或者命名为preSign更清晰）
                if sign == "+":
                    num = num  # 这里处理错了，num最后保存了sign中的"+"
                    stack.append(num)
                    # sign = "+"
                # elif c == "-":
                elif sign == "-":
                    num =  num * (-1)
                    stack.append(num)
                    # sign = "-"
                elif sign == "*":
                    stack[-1] = stack[-1] * num 
                    # 例如3+2*2：
                    # 扫描到*的时候，stack里边是[3,2]
                # elif c == "/":
                elif sign == "/":
                    # print(stack)
                    # print(s)
                    stack[-1] = stack[-1] // num
                num = 0
                sign = c
        print(stack)
        return sum(stack)
    # print(s)
    s = s.strip()
    res = calc(s)
    return res



# print(calculate("3 + 5 / 2"))
s = "3 + 5 / 2"
print(s.strip())