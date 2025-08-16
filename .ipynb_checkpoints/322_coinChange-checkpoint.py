# 第二遍刷到此题：几乎一遍通过
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = collections.defaultdict(int)
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0: dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] < float("inf") else -1

'''
def coinChange(coins: [int], amount: int) -> int:
    dp = [float('inf') for _ in range(amount+1)]      # 注意初始化不能用0 
    dp[0] = 0
    n = len(dp)
    m = len(coins)
    for i in range(1, n): # i是当前的找零总数
        for j in range(m):
            if i - coins[j] >= 0:   #注意判断条件
                dp[i] = min(
                    dp[i], 
                    dp[i-coins[j]] + 1
                )
    return dp[amount] if dp[amount] != float('inf') else -1 


print(coinChange([1, 2, 5], 11))
'''