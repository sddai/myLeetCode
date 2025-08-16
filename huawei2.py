def island(grid):
    def dfs(grid, i, j, visited):
        delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        if grid[i][j] != "1":
            return 
        # visited[i][j] = True
        for dx, dy in delta:
            x = i + dx
            y = j + dy
            # print(x, y)
            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if visited[x][y]:
                continue
            if grid[x][y] == "0":
                continue
            visited[x][y] = True
            dfs(grid, x, y, visited)
        return 
    
    m = len(grid)
    n = len(grid[0]) if grid else 0
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == "1":
                # print(i, j)
                dfs(grid, i, j, visited)
                cnt += 1
    return cnt
    


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(island(grid))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(island(grid2))

grid3 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["1","0","0","1","1"]
]
print(island(grid3))