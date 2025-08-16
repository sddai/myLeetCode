class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if s[0] in set([")", "}", "]"]):
            return False
        stack = [s[0]]
        for i in range(1, n):
            if s[i] == ")":
                if stack:
                    top = stack.pop()
                    if top == "(":
                        continue
                    else:
                        return False
                else:
                    return False
            elif s[i] == "]":
                if stack:
                    top = stack.pop()
                    if top == "[":
                        continue
                    else:
                        return False
                else:
                    return False
            elif s[i] == "}":
                if stack:
                    top = stack.pop()
                    if top == "{":
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        return  True
