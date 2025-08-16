# 此题第二次一遍通过
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        min_price = min(prices[0], prices[1])
        max_profit = prices[1] - prices[0] if prices[1] - prices[0] > 0 else 0
        for i in range(2, n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(prices[i], min_price)
        return max_profit
    

'''def maxProfit(prices: [int]) -> int:
    n = len(prices)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    # dp[0][i]表示当前的最低股价        
    # dp[1][i]表示当前节点卖出的最大利润
    for i in range(n):
        if i == 0:
            dp[0][i] = prices[0]
            dp[1][i] = 0
        else:
            dp[0][i] = min(prices[i], dp[0][i-1])
            dp[1][i] = max(prices[i] - dp[0][i], dp[1][i-1])
    return max(dp[1])

print(maxProfit([7,1,5,3,6,4]))    # 5
'''