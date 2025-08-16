class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def find(i, j, grid, start):
            if i >= m or i < 0 or j >= n or j < 0:
                return False
            if grid[i][j] == 1:
                return False
            if grid[i][j] == 0:
                grid[i][j] = 1
                find(i, j + 1, grid, start + 1)
                find(i + 1, j, grid, start + 1)
                find(i, j - 1, grid, start + 1)
                find(i - 1, j, grid, start + 1)
            return True
        m = len(grid)
        n = len(grid[0])
        start = 0
        # res = 0
        for i in range(m):
            find(i, 0, grid, 0)
            find(i, n - 1, grid, 0)
        for j in range(n):
            find(0, j, grid, 0)
            find(m - 1, j, grid, 0)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    find(i, j, grid, 0)
                # if grid[i][j] == 1 and not find(i, j, grid, 0):
                #     break
                # res += 1
        return res




        # def dfs(i, j, grid, path, res, start): # 起始用不到两个函数，统计封闭岛屿的逻辑跟统计靠边的岛屿的逻辑是一样的
        #     if i >= m or i < 0 or j >= n or j < 0:
        #         return 
        #     if used[i][j]:
        #         return 
        #     if grid[i][j] == 1:
        #         return 
        #     if grid[i][j] == 0:
        #         # used[i][j] = True
        #         dfs(i, j + 1, grid, start + 1)
        #         dfs(i + 1, j, grid, start + 1)
        #         dfs(i, j - 1, grid, start + 1)
        #         dfs(i - 1, j, grid, start + 1)
        #         # used[i][j] = False
