# dfs要注意合理地进行剪枝

# 此题第二遍一次通过
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if grid else 0
        def dfs(grid, i, j, start, path, min_path):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if i == m - 1 and j == n - 1:
                if min_path > path:
                    min_path = path
            path += grid[i][j]
            dfs(grid, i + 1, j, start + 1, path, min_path)
            dfs(grid, i, j + 1, start + 1, path, min_path)
            path -= grid[i][j]
        path = []
        min_path = float("inf")
        dfs(grid, 0, 0, 0, path, min_path)
        return min_path
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j, start, path):
            nonlocal min_path
            nonlocal ans
            if i >= m or j >= n or i < 0 or j < 0:
                return
            path += grid[i][j]   # 【注意】注意两个if和path累加的顺序：先判断出界，不出界就累加，累加之后判断是否是最小
            if path >= min_path[i][j]:
                return 
            min_path[i][j] = path
            if i == m - 1 and j == n - 1:
                ans = path
                return
            # for x, y in [[i + 1, j], [i, j + 1]]:   # 【效率问题】：把for循环改成并列的两行代码直接调用，就可以通过
                # dfs(x, y, start + 1, path)
            dfs(i+1, j, start + 1, path)
            dfs(i, j+1, start + 1, path)

        m = len(grid)
        n = len(grid[0]) if grid else 0        
        min_path = [[float("inf") for _ in range(n)] for _ in range(m)]
        ans = float("inf")
        path = 0
        dfs(0, 0, 0, path) 
        return ans


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:    
#         def dfs(grid, i, j, path, ans, vis):
#             if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
#                 return
#             path += grid[i][j]
#             if path >= vis[i][j]:
#                 return
#             vis[i][j] = path
#             if i == len(grid) - 1 and j == len(grid[i]) - 1:
#                 ans[0] = path
#                 return
#             dfs(grid, i+1, j, path, ans, vis)
#             dfs(grid, i, j+1, path, ans, vis)
#         ans = [float('inf')]
#         vis = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
#         dfs(grid, 0, 0, 0, ans, vis)
#         return ans[0]
