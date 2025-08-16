class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True
        n = len(piles)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[i][0]先手, dp[i][1]后手
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        #  dp[i][j][*]表示从剩余i～j段取石子
        for i in range(n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n): # 注意这里，是个三角矩阵，j从i或者i+1开始遍历
            # 【讨论】：为什么j的取值从i+1到n-1？
            # dp为什么是上三角？
            # i～j是某一轮次的结果，则其上一轮次应该是i-1～j或者i～j+1，所以是上三角
                left = dp[i + 1][j][1] +  piles[i]
                right = dp[i][j - 1][1] + piles[j]
                if left > right:
                    dp[i][j][0] = left
                    # dp[i][j][1] = dp[i + 1][j][0] + piles[j]   # 后手在i～j处不再拿棋子
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    # dp[i][j][1] = dp[i][j - 1][0] + piles[i]
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] > dp[0][n - 1][1]
        

