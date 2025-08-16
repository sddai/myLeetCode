# 在这个区间递归中，i，j分别表示区间的左右端点
# span in range(2, n + 1)   ->   i in range(n - span + 1)   ->   j = i + span - 1
# 上述关系展开之后，就是：
# 1. 区间宽度span = 2, 此时i取[0, 1, 2, 3, 4], j取[1, 2, 3, 4, 5]
# 2. 区间宽度span = 3, 此时i取[0, 1, 2, 3], j取[2, 3, 4, 5]
# 3. 区间宽度span = 4，此时i取[0, 1, 2], j取[3, 4, 5]
# 这样的计算顺序可以保证在计算 dp[i][j] 时，状态转移方程中的状态 dp[i + 1][j]，dp[i][j - 1] 和 dp[i + 1][j - 1] 均已计算过。
# 这是由于，i+1和j-1其实就是使得span减1，因此在此dp中让span递增
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for span in range(2, n+1):
            for i in range(n-span+1):
                j = i + span -1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i+1][j] + 1, 
                        dp[i][j-1] + 1
                    )
        return dp[0][n-1]
        


# class Solution:
#     def minInsertions(self, s: str) -> int:
#         n = len(s)
#         dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 dp[i][j] = max(
#                     dp[i-1][j], 
#                     dp[i][j-1]
#                 )
#                 if s[i-1] == s[n-j]:
#                     dp[i][j] = max(
#                         dp[i][j], 
#                         dp[i-1][j-1] + 1
#                     )
#         return n - dp[n][n]