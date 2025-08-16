# 此题易错之处在于如何处理全局变量和局部变量
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(graph, i, onPath, visited):
            # onPath = self.onPath
            # visited = self.visited
            # hasCircle = self.hasCircle
            if onPath[i]:
                self.hasCircle = True    # 如果这里出现hasCircle，那么这个变量会成为局部变量，也就是说全局的hasCircle不会一起随着变化，建议使用self定义全局变量
                # return 
            if visited[i] or self.hasCircle:
                return 
            onPath[i] = True
            visited[i] = True
            for neighbor in graph[i]:
                # visited[neighbor] = True
                # if onPath[neighbor] == True:   # 应该在进入一个节点之后就判断这个点在不在path上边
                #     hasCircle = True
                #     return 
                dfs(graph, neighbor, onPath, visited)
            onPath[i] = False # 回溯

        graph = defaultdict(list)
        self.hasCircle = False
        for sub, pre in prerequisites:
            graph[pre].append(sub)
        visited = [False] * (numCourses)
        onPath = [False] * (numCourses)
        for i in range(numCourses):
            # if not self.visited[i]: # 
                # onPath = [False] * (numCourses)   # onPath用一个全局的
            dfs(graph, i, onPath, visited)
        
        return not self.hasCircle