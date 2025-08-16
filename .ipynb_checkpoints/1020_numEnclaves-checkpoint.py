# 此题几乎一遍通过
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, start, used):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if used[i][j]:
                return
            if grid[i][j] == 0:
                return 
            if grid[i][j] == 1:
                # path.append()
                grid[i][j] = 0
            used[i][j] = True
            dfs(i, j + 1, start + 1, used)
            dfs(i + 1, j, start + 1, used)
            dfs(i, j - 1, start + 1, used)
            dfs(i - 1, j, start + 1, used)
            used[i][j] = False
        m = len(grid)
        n = len(grid[0]) if grid else 0
        used = [[False] * n for _ in range(m)]
        for i in range(m):
            dfs(i, 0, 0, used)
            dfs(i, n - 1, 0, used)
        for j in range(n):
            dfs(0, j, 0, used)
            dfs(m - 1, j, 0, used)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt