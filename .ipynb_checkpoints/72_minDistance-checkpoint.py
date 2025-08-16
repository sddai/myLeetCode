# 错在没有考虑空字符串的情况，所以dp要预留出来dp[0][0]作为空字符串——dp维度设置为n+1,m+1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0: return m
        if m == 0: return n
        dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
        # dp[0][0] = 0 if word1[0] == word2[0] else 1
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][j - 1] + 1, # 插入
                    dp[i - 1][j] + 1, # 删除
                    dp[i - 1][j - 1] + 1, # 替换
                )
        return dp[-1][-1]


# 错在没有考虑空字符串的情况，所以dp要预留出来dp[0][0]作为空字符串——dp维度设置为n+1,m+1
'''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0: return m
        if m == 0: return n
        dp = [[float("inf") for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0 and word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][j - 1] + 1, # 插入
                    dp[i - 1][j] + 1, # 删除
                    dp[i - 1][j - 1] + 1, # 替换
                )
        return dp[-1][-1]
'''