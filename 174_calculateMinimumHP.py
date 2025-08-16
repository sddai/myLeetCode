class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0]) if dungeon else 0
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] =  - dungeon[m - 1][n - 1] + 1 if dungeon[m - 1][n - 1] < 0 else 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if not (i == m - 1 and j == n - 1):
                    res = min(
                        dp[i][j + 1] - dungeon[i][j], 
                        dp[i + 1][j] - dungeon[i][j] 
                    )
                    dp[i][j] = max(1, res)
        return dp[0][0]

        # ans = -float("inf")

        # for i in range(m):
        #     for j in range(n):
        #         if i >= 0 and i < m and j >= 0 and j < n:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + dungeon[i][j]
        #             ans = max(ans, - dp[i][j] + 1 )
        return ans

'''chatgpt:
class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # initialize the dp matrix with infinity
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        # set the bottom-right corner to 1 or -grid[m-1][n-1] + 1
        dp[m - 1][n - 1] = 1 if grid[m - 1][n - 1] >= 0 else -grid[m - 1][n - 1] + 1
        # fill the dp matrix from bottom to top and right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # skip the bottom-right corner
                if i == m - 1 and j == n - 1:
                    continue
                # find the minimum health needed from the right and down cells
                res = min(dp[i][j + 1], dp[i + 1][j]) - grid[i][j]
                # update the dp matrix with the maximum of 1 and res
                dp[i][j] = max(1, res)
        # return the top-left corner as the answer
        return dp[0][0]

'''