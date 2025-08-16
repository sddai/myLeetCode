# 注意多层括号嵌套的问题
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def decodeString(self , s: str) -> str:
        def get_num(s: str):
            num = 0
            i = 0
            while i < len(s):  
                if s[i].isdecimal():
                    num = num * 10
                    num += int(s[0])
                    i += 1
                else:
                    break
            return [num, i]
        res = []
        n = len(s)
        i = 0
        stack = []
        curr_str = ""
        curr_num = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0
            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += c
            i += 1
        return curr_str

        # # write code here
        # def get_num(s: str):
        #     num = 0
        #     i = 0
        #     while i < len(s):  
        #         if s[i].isdecimal():
        #             num = num * 10
        #             num += int(s[0])
        #             i += 1
        #         else:
        #             break
        #     return [num, i]
        # res = []
        # n = len(s)
        # i = 0
        # # for i, c in enumerate(s):
        # while i < n:
        #     c = s[i]
        #     if not c.isdecimal():
        #         res.append(c)
        #         i += 1
        #     else:
        #         num, count = get_num(s[i:])
        #         i += count + 1
        #         multi = []
        #         start = i
        #         while i < n and s[i] != "]":
        #             multi.append(s[i])
        #             i += 1
        #         end = i
        #         for time in range(num):
        #             res.append(s[start:end])
        #         i += 1

        # return "".join(res)

        

