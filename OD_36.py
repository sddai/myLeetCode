def heros(m, n, grid):
    visited = [[False] * n for _ in range(m)]
    dfs(grid, 0, 0, visited)
    zeros = 0
    twos = 0
    grid[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                zeros += 1
            if grid[i][j] == 2:
                twos += 1
    # print(visited)
    return zeros + twos


def dfs(grid, i, j, visited):
    if grid[i][j] == 0:
        grid[i][j] = 1
    visited[i][j] = True
    print(i, j)
    for x, y in [[i, j - 1], [i - 1, j], [i, j + 1], [i + 1, j]]:
        if x < 0 or y < 0 or x >= m or y >= n:
            continue
        if visited[x][y]:
            continue
        if grid[x][y] == 2:
            continue
        dfs(grid, x, y, visited)


# m, n = list(map(int, input().split()))
# grid = [list(map(int, input().split()))  for _ in range(m)]
m, n = [4, 4]
grid = [[0, 0, 0, 0], [0, 2, 2, 2], [0, 2, 0, 0], [0, 2, 0, 0]]
print(heros(m, n, grid))