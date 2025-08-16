class Solution:
    def calculate(self, s: str) -> int:
        def calc(s):
            # i = 0
            num = 0
            sign = 1
            stack = []
            print(s)
            for c in s:
                print("c: ", c)
                # c = s[i]
                if c.isdigit():
                    num = num * 10 + (ord(c) - ord("0"))
                    # num = num * sign # 处理每一位，处理过后统一加符号
                    # stack.append(num)
                else:
                    if c == "+":
                        num = num * sign
                        stack.append(num)
                        sign = 1
                    elif c == "-":
                        num =  num * sign
                        stack.append(num)
                        sign = -1
                    elif c == "*":
                        stack[-1] = stack[-1] * num 
                    elif c == "/":
                        print(stack)
                        print(s)
                        stack[-1] = stack[-1] // num
                    num = 0
                    # sign = 1
            return sum(stack)
        print(s)
        s = s.strip()
        res = calc(s)
        return res
