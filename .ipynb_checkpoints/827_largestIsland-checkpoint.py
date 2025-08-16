
def largestIsland( grid: [[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    colors = [[0]*n for i in range(m)] # 给连成一片的岛屿染成同种颜色
    color = 0
    area = dict()   # 记录每个岛屿的面积
    def getArea(i:int, j:int) -> int:
        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if (x >=0 and y >= 0 and x < m and y < n) and grid[x][y] == 1  and colors[x][y] == 0:
                colors[x][y] = color
                area[color] += 1
                getArea(x, y)
        return area[color]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and colors[i][j] == 0:
                color += 1
                colors[i][j] = color
                area[color] = 1
                getArea(i, j)
    print(area)
    ans = 0
    ans = max(area.values(), default=0)
    print(area.values())
    # visitedColor = set([0])   # 自己写的时候，这句话的位置放错了。分析：每次进入循环，每当找到一个新的0，计划翻转成1，这个时候的visited需要重新计算，因为上次找到的visited对于下一次要反转的0来说是没有访问过的
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                visitedColor = set([0])
                newArea = 1
                for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if (x >=0 and y >= 0 and x < m and y < n) and (colors[x][y] not in visitedColor):
                        visitedColor.add(colors[x][y])
                        newArea += area[colors[x][y]]
                ans = max(ans, newArea)

    return ans


