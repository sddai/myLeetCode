# 此题几乎一遍通过
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(n):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + matrix[i][j])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1] + matrix[i][j])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
        ans = float("inf")
        for j in range(n):
            if ans > dp[m-1][j]:
                ans = dp[m-1][j]
        return ans