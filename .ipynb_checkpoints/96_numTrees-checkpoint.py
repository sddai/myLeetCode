# 递归超时，用动态规划
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[i]表示1～n能构成的BST数目
        # dp[n]分为一个根、1～i-1、i+1～n：即for...dp[i] = dp[i-1] * dp[n-i]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            # for k in range(i, n + 1):
            for k in range(1, i + 1):
                dp[i] += dp[k - 1] * dp[i - k]
        return dp[-1]

        # dp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = 1

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         dp[i][j] = dp[][]

    #     # self.res = 1
    #     res = self.dfs(1, n)
    #     return res
    #     # return self.res
    # def dfs(self, left, right):       【超时】
    #     print(left, right)
    #     if left > right:
    #         return 1
    #     res = 0
    #     for i in range(left, right + 1):  # 注意：i是根节点，所以两半分别是l～i-1，以及i+1～right
    #         l = self.dfs(left, i - 1)
    #         r = self.dfs(i + 1, right)
    #         res += l * r
    #     return res