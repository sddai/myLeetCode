# 这是一道【状态机】问题
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)] 
        # dp[i][0]表示第i天卖出(或者不持有股票)  dp[i][1]表示第i天买进（或者持有股票）
        # 三种状态：买入、卖出、持有
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):   # 注意i从1开始
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1])