class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        K = k * 2
        n = len(prices)
        # dp = [[[-float("inf")] * 2 for _ in range(2 * K + 1)] for _ in range(n)]
        dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(n)]
        # dp[i][k][0]不持有股票，dp[i][k][1]持有股票
        # dp[0][0][0] = 0
        # dp[0][1][0] = 0
        # dp[1][0][0] = 0
        # 【注意初始化】base case
        for i in range(n):
            dp[i][0][1] = -float("inf")
            dp[i][0][0] = 0
        for k in range(K + 1):   # 注意思考这里的base case：对于后边的两层for循环，每一个k都会遇到i==0的情况
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(1, n):
            for k in range(1, K + 1):
                # if i == 0 and k == 1:
                #     dp[0][1][0] = 0
                #     dp[0][1][1] = -prices[0] 
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # print(dp)
        return dp[n - 1][K][0]