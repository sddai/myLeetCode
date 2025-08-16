class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j, grid1, grid2, ):
            # if i <= 0 or i >= m or j <= 0 or j >= n:  # 这里错了，i==0是有效的
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            # if used[i][j]:
            #     return False
            # if grid1[i][j] == 0:
                # return False
            if grid2[i][j] == 0:
                return False
            # used[i][j] = True
            grid2[i][j] = 0
            dfs(i, j + 1, grid1, grid2, )
            dfs(i + 1, j, grid1, grid2, )
            dfs(i, j - 1, grid1, grid2, )
            dfs(i - 1, j, grid1, grid2, )
            # used[i][j] = False
            # return 
        m = len(grid1)
        n = len(grid1[0])
        # used = [[False] * n for _ in range(m)]
        # res = 0
        # 先把对应grid1中为水域的个grid2岛屿沉下去
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j, grid1, grid2)
        res = 0
        for i in range(m):
            for j in range(n):
                # if grid2[i][j] == 1 and not used[i][j]:
                # if grid2[i][j] == 1 and grid1[i][j] == 1:
                if grid2[i][j] == 1:
                    res += 1
                    dfs(i, j, grid1, grid2)
        return res