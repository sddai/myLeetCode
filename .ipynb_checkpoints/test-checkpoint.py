def diffWaysToCompute(expression: str) -> [int]:
    def helper(expression):
        n = len(expression)
        # if n == 1 and expression[0] not in set(["+", "-", "*"]):  #【注意】这里会有两位数的数字：比如expression = "11"
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i in range(n):
            curr = expression[i]
            if expression[i] in set(["+", "*", "-"]):
                left = helper(expression[:i])
                right = helper(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            ans.append(l + r)
                        elif expression[i] == "-":
                            ans.append(l - r)
                        elif expression[i] == "*":
                            ans.append(l * r)
        return ans

    # ans = []
    ans = helper(expression)    
    return ans 


print(diffWaysToCompute("3*4+2*3"))