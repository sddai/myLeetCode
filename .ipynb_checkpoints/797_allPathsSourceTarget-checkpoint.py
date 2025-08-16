# 回溯
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def dfs(graph, n, curr, start, res, path):
            path.append(curr)  # 进入一层回溯时，首先将本节点加入path
            if curr == n - 1:
                # return res
                res.append(path[:])  # 注意深浅拷贝
                # 不 return 也可以，因为图中不包含环，不会出现无限递归
            # path = []
           
            for neighbor in graph[curr]:
                # path.extend(dfs(graph, n, neighbor, start + 1, res))  #策略：不用返回值，直接在全局变量上修改
                # if path: path.pop()
                dfs(graph, n, neighbor, start + 1, res, path)
            path.pop()
            # return path
        res = []
        path = []
        dfs(graph, n, 0, 0, res, path)
        return res
    
# 第二次：
# 回溯,一次通过
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def dfs(node,  onPath, path, res):
            # if visited[node]:
            #     return 
            # visited[node] = True
            onPath[node] = True
            path.append(node)
            if node  == n - 1:
                res.append(path[:])
            for neighbor in graph[node]:
                # if not visited[neighbor]: 
                dfs(neighbor, onPath, path, res)
            onPath[node] = False
            path.pop()
        # visited = [False] * n
        onPath = [False] * n
        path = []
        res = []
        dfs(0,  onPath, path, res)
        return res
