class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1 for _ in range(n+1)] # dp[i]表示前i个点进行分割以后的最大和
        dp[0] = 0
        for i in range(1, n+1):
            max_val = arr[i-1]    # 这两个都能通过
            # max_val = 0   # 这两个都能通过
            for j in range(1, k+1):   # 枚举j的所有可能值，j表示最后边的j个元素划分为一组，所以0<j<=k
                if i-j >= 0: # 之前写的时候这里多了一个i-j-1，注意j代表最后j个数字作为一组，这一组中包括i号元素
                    max_val = max(max_val, arr[i-j])
                    dp[i] = max(
                        dp[i], 
                        dp[i-j] + max_val * j
                    )
        return dp[-1]
        # n = len(arr)
        # # dp = [[-1 for _ in range(n + 1)] for _ in range(n+1)]
        # dp[0][0] = 0
        # dp[1][1] = arr[0]
        # for i in range(1, n+1):
        #     cnt = 0
        #     mx = 0
        #     for j in range(1, i+1):
        #         # mx = max(mx, dp[i-1][j-1])
        #         # dp[i][j] = max(dp[i][j-1], mx)       