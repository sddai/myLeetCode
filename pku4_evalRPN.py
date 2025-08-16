def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    # currToken = tokens[0]
    if len(tokens) == 1:
        return int(tokens[0])
    for i, currToken in enumerate(tokens):
        # print(stack)
        if currToken.isdecimal() == True or (currToken[0]=="-" and currToken[1::].isdecimal()== True):
            stack.append(int(currToken))
        elif currToken in set(["+", "-", "*", "/"]):
            num1 = int(stack.pop())
            # if len(stack) == 0:
            #     return num1
            # else:
            num2 = int(stack.pop())
            if currToken == "+":
                ans = num2 + num1
            if currToken == "-":
                ans = num2 - num1
            if currToken == "*":
                ans = num2 * num1
            if currToken == "/":
                if (num1) * (num2) >= 0:    # 这里写错了，应该是判断政府，而不是取绝对值
                    ans = abs(num2) // abs(num1)
                else:
                    ans = -1 * (abs(num2) // abs(num1))  #注意后两项外边要加括号，否则还是处理负数除法
            stack.append(int(ans))
        # currToken = stack.pop()
    ans = stack.pop()
    # print(6//(-132))
    # currToken = "-2"
    # print((currToken in set(["+", "-", "*", "/"])))
    # num1 = -132
    # num2 = 6
    # print(abs(num2) // abs(num1))
    return ans

"""
通过测试用例：
12 / 20
输入：
["4","-2","/","2","-3","-","-"]
输出：
-3
stdout
[]
['4']
['4', '-2']
[2]
[2, '2']
[2, '2', '-3']
[2, 5]
2

预期结果：
-7

说明除法处理的不对
"""
