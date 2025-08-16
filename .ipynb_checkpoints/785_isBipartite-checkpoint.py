def isBipartite(graph: [[int]]) -> bool:
    n = len(graph)
    # visited = [0 for _ in range(n)] 
    color = [0 for _ in range(n)]
    q = []
    for i, neighbors in enumerate(graph):
        if color[i] == 0:
            q.append(i)
            color[i] = 1   ###########易错###########
            # for neighbor in neighbors:
                # q.append(neighbor)
            while q:
                curr = q.pop(0)
                # color[curr] = 1 ###################本题错在染色位置不对，遍历到一个未染色的节点之后马上染色
                # for neighbor in neighbors:  #######这里易错，不要写成in neighbors
                for neighbor in graph[curr]:
                    if color[neighbor] == color[curr] and color[curr] != 0:
                        return False
                    if color[neighbor] != color[curr] and color[neighbor] == 0:
                        color[neighbor] = -color[curr]
                        q.append(neighbor)
    return True


print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

'''
总结：
最外层遍历所有节点，避免有孤立节点（不与其他节点连通的点）
第一个未染色的点就是起始点：
1. 先把这个起始点染色，并加入队列
2. 遍历队列：
3. q出队列，记作curr
4. 判断是否染色冲突：
5. 如不冲突：染色，neighbor入队列
   如冲突：return False
'''

# 第二次使用另一种解法（dfs）：
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.n = len(graph)
        self.color = [1] * self.n
        self.visited = [False] * self.n
        self.valid = True
        for node in range(self.n):
            self.dfs(graph, node)
        return self.valid
    def dfs(self, graph, node):
        if not self.valid:
            return False
        self.visited[node] = True
        for neighbor in graph[node]:
            if not self.visited[neighbor]:
                self.color[neighbor] = -self.color[node]
                self.dfs(graph, neighbor)
            else:
                if self.color[node] == self.color[neighbor]:
                    self.valid = False
                else:
                    continue
