# 本题用分治思想：每个分支返回一个列表，处理过程的核心就是遍历返回的这个列表里边的每一种可能
# 对于一个表达式例如："1+2*3"来说，helper(expression)里边的for循环会依次扫描到两个运算符"+"和"*"，在这两次循环中，ans分别被append上了以这两个运算符计算出来的结果，也就是先计算+和先计算*的结果都在append的那个list里边，最后返回给上一层的也是这个ans
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(expression):
            n = len(expression)
            # if n == 1 and expression[0] not in set(["+", "-", "*"]):  #【注意】这里会有两位数的数字：比如expression = "11"
            if expression.isdigit():
                return [int(expression)]
            ans = []
            for i in range(n):
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

    
# 本题第二次一遍通过
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(expression):
            res = []
            if expression.isdigit():
                return [int(expression), ]
            for i in len(expression):
                c = expression[i]
                if c not in set(["+", "-", "*"]):
                    continue
                left = helper(expression[:i])
                right = helper(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == "+":
                            res.append(l + r)
                        elif c == "-":
                            res.append(l - r)
                        elif c == "*":
                            res.append(l * r)
            return res
        ans = helper(expression)
        return ans
