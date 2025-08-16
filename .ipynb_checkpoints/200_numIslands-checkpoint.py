# 此题一遍通过
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j]:
                return False
            if grid[i][j] != "1":
                return False
            visited[i][j] = True
            for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(grid, i, j)
            return True 
                
            
        m = len(grid)
        n = len(grid[0]) if grid else 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(grid, i, j): cnt += 1
        return cnt
            


