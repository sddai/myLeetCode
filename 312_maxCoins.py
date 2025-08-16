# 此题一遍通过
# dp[i][j] = x 表示，戳破气球 i 和气球 j 之间（开区间，不包括 i 和 j）的所有气球，可以获得的最高分数为 x。
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[-float("inf")] * (n + 2) for _ in range(n + 2)]
        for i in range(n + 1):
            dp[i][i + 1] = 0
        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], 
                        dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j]
                    )
        return dp[0][n + 1]