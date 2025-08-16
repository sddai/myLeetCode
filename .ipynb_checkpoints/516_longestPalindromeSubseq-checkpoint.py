# 注意区分dp数组的维度，什么时候初始化成n维，什么时候是n+1维
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n) for _ in range(n)] # i, j是双指针
        dp[0][0] = 0 
        for i in range(n):
            dp[i][i] = 1
        # for l in range(2, n + 1):
        #     for i in  range(1, n - l + 1): # i 表示下标+1（序号）
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                # j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # 【易错】：两个符号不都是加好，i,j从两边项中间收缩，所以i递增，j递减
        # print(dp)
        return dp[0][-1]