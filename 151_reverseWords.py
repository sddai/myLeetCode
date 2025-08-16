class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split("")   # 这里不加空格s = s.split(" ")，就可以避免分出来空格的问题
        n = len(s)
        matrix = [[] for _ in range(n)]
        p = 0
        for word in s:
            # matrix[p].append(s[])
            for c in word:
                matrix[p].append(c)
            # print(p, n)
            p += 1
        ans = []
        m = len(matrix)
        for i in range(m):
            # for c in matrix[m - 1 - i]:
            tmp = "".join(matrix[m - 1 - i])
            if tmp and tmp[0] != " ":
                ans.append(tmp)
        return " ".join(w for w in ans)
            # print(word)
            # if word and word[0] != " ":
            #     ans = " ".join(word)
        return ans

        # l = 0
        # r = n - 1
        # while l <= r:
        #     if " " not in s[l] and " " not in s[r]:
        #         s[l], s[r] = s[r], s[l]
        #     # if " " not in s[l]:
        #     #     r -= 1
        #     # if " " not in s[r]:
        #     #     l += 1
        #     l += 1
        #     r -= 1
        # return " ".join(w for w in s)

# 题解： “字符串分割”、“列表倒序” 的内置函数 （面试时不建议使用）
# s = "labuladong world hello"
# 正确的做法是，先将整个字符串 s 反转：
# s = "gnodalubal dlrow olleh"
# 然后将每个单词分别反转：
# s = "labuladong world hello"