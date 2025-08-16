class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = defaultdict(int)
        # count = dict()
        for c in s:
            count[c] += 1
        stack = []
        inStack = defaultdict(bool)
        for c in s:
            count[c] -= 1   # 注意这句话要在continue的前边
            if inStack[c]:  # 在考虑字符 s[i] 时，如果它已经存在于栈中，则不能加入字符 s[i]
                continue
            # 如果c在栈中，则从上一个c到当前这个c之间，加入栈中的元素都应该是比c大的，所以在这两个c中间，应该保留前边那个c，因此只要instack为True就不必再讨论重复的字符了
            # while stack and stack[-1] > c and count[c] > 0: # 【易错！】
            # while stack and stack[-1] > c and count[stack[-1]] > 0: 
            while stack and stack[-1] > c:
                if count[stack[-1]] == 0:
                    break
                p = stack.pop()
                inStack[p] = False
            stack.append(c)
            inStack[c] = True
        return "".join(stack)


    # def smallestSubsequence(self, s: str) -> str:
    #     stk = []

    #     # 维护一个计数器记录字符串中字符的数量
    #     # 因为输入为 ASCII 字符，大小 256 够用了
    #     count = [0] * 256
    #     for i in range(len(s)):
    #         count[ord(s[i])] += 1

    #     in_stack = [False] * 256
    #     for c in s:
    #         # 每遍历过一个字符，都将对应的计数减一
    #         count[ord(c)] -= 1

    #         if in_stack[ord(c)]: continue

    #         while stk and stk[-1] > c:
    #             # 若之后不存在栈顶元素了，则停止 pop
    #             if count[ord(stk[-1])] == 0:
    #                 break
    #             # 若之后还有，则可以 pop
    #             in_stack[ord(stk.pop())] = False

    #         stk.append(c)
    #         in_stack[ord(c)] = True

    #     return ''.join(stk)
 