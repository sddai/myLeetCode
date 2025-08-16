class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                    # continue
                else:
                    # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - coins[i - 1]]
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[-1][-1]
    
'''
一个调试运行结果如下： print(change(5, [1, 2, 5]))
i = 1
    j = 1
    dp[1][1] = 1
    j = 2
    dp[1][2] = 1
    j = 3
    dp[1][3] = 1
    j = 4
    dp[1][4] = 1
    j = 5
    dp[1][5] = 1
i = 2
    j = 1
    dp[2][1] = 1
    j = 2
    dp[2][2] = 2
    j = 3
    dp[2][3] = 2
    j = 4
    dp[2][4] = 3
    j = 5
    dp[2][5] = 3
i = 3
    j = 1
    dp[3][1] = 1
    j = 2
    dp[3][2] = 2
    j = 3
    dp[3][3] = 2
    j = 4
    dp[3][4] = 3
    j = 5
    dp[3][5] = 4
4
'''