# 注意：本文是求长度，不是返回字符串
# 【dp的长度】dp的长度设置为n+1

# 【dp数组的空间优化】降维
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [0 for _ in range(n2 + 1)]
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1
        pre = dp[0]
        
        for i in range(1, n1 + 1):
            pre = 0
            for j in range(1, n2 + 1):
                temp = dp[j] # dp从左向右更新，此时还没有更新，所以此时的dp[j]是上一轮[i-1]时候的dp[i-1][j]，我们把它记录下来
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = max(dp[j], pre + 1) # pre 是上一轮也就是[j-1]时候记录下来的，所以pre就是dp[i-1][j-1]
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[-1]


'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
'''