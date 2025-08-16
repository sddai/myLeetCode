# 注意循环中k的取值从2开始
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        K = k
        cost = [[0 for _ in range(n)] for _ in range(n)]  
        # for i in range(n):
        #     cost[i][i] = 0
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                cost[i][j] = cost[i+1][j-1] if s[i] == s[j] else cost[i+1][j-1] + 1  # 注意这里不要写错为i-1,j+1
        # dp[i][k]表示把前i个字符分成k份的最小cost
        dp = [[float("inf") for _ in range(K + 1)] for _ in range(n)]   # 如果使用C++，则需要用INT_MAX//2防止溢出，因为后边有加法，但是Python不需要
        # dp = [[0 for _ in range(K+1)] for _ in range(n)]
        # dp[0][0] = 0
        # for i in range(n):
        for i in range(n):   # 注意i是否取到0
            # for k in range(1, K + 1):
            dp[i][1] = cost[0][i]
            # for k in range(2, min(K, i) + 1):  # k至少要取2，而不是1，因为初始化的时候是初始化了所有的k=1的情况（直接等于cost），所以这里从k=2开始
            for k in range(2, K + 1):
                # for j in range(k-1, i):   # j表示将前j个字符分成k-1份，因此j必须大于等于k-1（不采取这种思路）
                for j in range(i): 
                    # dp[i][1] = cost[0][i] # 这句话放在循环外边
                    dp[i][k] = min(
                        dp[i][k], 
                        dp[j][k-1] + cost[j+1][i]
                    )
        return dp[n-1][K]


'''
        n = len(s)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     cost[i][i] = 0
        # for i in range(n):
        #     for j in range(n):
        for length in range(2, n + 1):  # 这里易错！！length是可以取到n的
            for i in range(0, n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] if s[i] == s[j] else cost[i+1][j-1] + 1
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        #dp[i][k]: k <= i  , 前i个字符分为k份
        dp[1][1] = 1

        for i in range(1, n+1):
            for k_i in range(1, k + 1):
                for j in range(1, i + 1):   # 这里不要把j定义成分界点坐标，直接将j定义为上一轮前j个点视为k_i-1组，本轮从j+1号点开始到i处作为一组
                # 在循环里，dp的初始化过程为：dp[i][1] = cost[0][i]，表示前i个化成一组，相当于前i个直接变换回文的cost
                    # dp[i][k_i] = dp[i - j][k_i - 1] + cost[i-j][j]

'''