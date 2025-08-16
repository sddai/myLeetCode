class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # avg[i][j] 用累加和来求
        n = len(nums)
        avg = [0 for _ in range(n)]
        avg[0] = nums[0]
        for i in range(1, n):
            avg[i] = nums[i] + avg[i - 1]
        # sum[i][j] = avg[j] - avg[i-1] if i > 0 else avg[j]
        def sumOf(i, j):
            return avg[j] - avg[i-1] if i > 0 else avg[j]
        K = k
        dp = [[-float("inf") for _ in range(K + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = float(sumOf(0, i)) / (i + 1) 
            for k in range(2, K + 1):
                for j in range(i):
                    dp[i][k] = max(
                        dp[i][k], 
                        # dp[j][k-1] + sumOf(j + 1, i)   # 注意这里是求均值不是求和
                        dp[j][k-1] + float(sumOf(j + 1, i)) / (i - j)
                    )
        # print(dp)
        return dp[n-1][K]