class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if used[i][j]:
                return 0
            if grid[i][j] == 0:
                return 0
            area = 1
            used[i][j] = True
            area += dfs(grid, i, j + 1, path)
            area += dfs(grid, i + 1, j, path)
            area += dfs(grid, i, j - 1, path)
            area += dfs(grid, i - 1, j, path)
            return area
        m = len(grid)
        n = len(grid[0])
        res = 0
        used = [[False] * n for _ in range(m)]
        path = 0
        ans = []
        for i in range(m):
            for j in range(n):
                if not used[i][j] and grid[i][j] == 1:
                # if  grid[i][j] == 1:
                    # res += 1
                    # dfs(grid, i, j, path)  # 这里，path只是把值传进了函数dfs，dfs对path的操作没有改变外层函数中的path变量
                    area = dfs(grid, i, j, path)
                    ans.append(area)
                    # path = 0
        return max(ans) if ans else 0