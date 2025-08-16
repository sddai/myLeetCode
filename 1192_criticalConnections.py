class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        timestamp = 0
        graph = collections.defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        dfn = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        ans = []

        def tarjan(curr, parent, timestamp): 
            dfn[curr] = timestamp
            low[curr] = timestamp
            for child in graph[curr]:
                if child == parent:   # 类似于visited
                    continue
                if dfn[child] == -1:
                    tarjan(child, curr, timestamp + 1)
                    if dfn[curr] < low[child]:#low[child]是指子节点能回溯到的最远的父节点，如果子节点回溯不到当前curr的序号，说明这段连接是桥
                        ans.append([curr, child])
                low[curr] = min(low[child], low[curr]) # 就是一个dfs的后序遍历，相当于入栈再回溯的过程
        tarjan(0, -1, 0)
        return ans
