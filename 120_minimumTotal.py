# TODO dp化成一维数组
# 注意考虑没有意义的状态，例如，对于第i行最后一个元素dp[i][j]来说，dp[i - 1][j]是无意义的
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[float("inf") for _ in range(m)] for _ in range(n)]
        dp[0][0] = triangle[0][0]
        # for i in range(n + 1):
        #     dp[i][0] = 0
        # for j in range(m + 1):
        #     dp[0][j] = 0
        for i in range(1,  n):  # 这里注意从1开始 ,否则对于i=0，j=0，后边dp的下标i-1会导致取到dp[-1][-1],产生错误结果，这里也可以用一个if判断i，j的范围
            for j in range( i + 1):   # 这里要注意j和i的关系 
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])
        # print(dp)
        ans = float("inf")
        for j in range(0, m):
            ans = min(ans, dp[-1][j])
        return ans