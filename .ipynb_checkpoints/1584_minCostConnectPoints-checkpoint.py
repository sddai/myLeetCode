# 第二次一遍通过
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class UF:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.count = n
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def isConnected(self, x, y):
                return self.find(x) == self.find(y)
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    # self.parent[y] = self.find(x)  # 这句话注意：union操作的是y的根换成x的根，否则会成环
                    self.parent[root_y] = root_x
                    self.count -= 1
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                cost = abs(xi - xj) + abs(yi - yj)
                edges.append([i, j, cost])
        edges.sort(key = lambda x: x[2])
        mst = UF(n)
        total_cost = 0
        for i, j, cost in edges:
            if not mst.isConnected(i, j):
                mst.union(i, j)
                total_cost += cost
        # if mst.count == 1:
        return total_cost

