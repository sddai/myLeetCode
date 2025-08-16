class Solution:
    def fib(self, n: int) -> int:
        # 【解法三】进一步优化存储空间（此种方法分数最高）——滚动存储
        dp_0 = 0
        dp_1 = 1
        if n <= 1: return n
        for i in range(2, n + 1):
            t = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = t
            print(dp_1)
        return dp_1

        # 【解法二】使用dp table
        # dp = [0 for _ in range(n + 1)]   # 这种方法更快
        # if n <= 1: return n
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]


        # 【解法一】此解法已通过
        # def helper(i, dp):
        #     if dp[i] != -float("inf"):
        #         return dp[i]
        #     if i == 1 or i == 2:
        #         return 1
        #     return helper(i - 1, dp) + helper(i - 2, dp)

    
        # # N = 20
        # if n == 0: return 0
        # dp = [-float("inf") for _ in range(n + 1)]
        # return helper(n, dp)