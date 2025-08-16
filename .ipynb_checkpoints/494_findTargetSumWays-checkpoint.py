# 背包问题——目标和类型题
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total + target < 0 or (total + target) % 2 == 1: return 0
        T = (total + target) // 2
        dp = [[0] * (T + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(T + 1):
                # if nums[i - 1] > :
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]