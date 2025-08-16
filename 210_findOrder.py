class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]
        self.graph = self.graph
        for sub, pre in prerequisites:
            self.graph[pre].append(sub)
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        self.res = []
        self.valid = True
        for i in range(numCourses):
            if not self.visited[i] and self.valid:
                self.dfs(self.graph, i)                
        self.res.reverse()
        print(self.valid)
        return self.res if self.valid else []

    def dfs(self, graph, i):
        print(i)
        if self.onPath[i] == True:
            self.valid = False
            return
        self.visited[i] = True
        self.onPath[i] = True
        for neighbor in graph[i]:
            if not self.visited[neighbor]:
                self.dfs(graph, neighbor)
                # if not self.valid:
                #     return
            elif self.onPath[neighbor] == True:  # 有一种情况需要考虑到：即，已经visited，这里边有可能有onpath的，这时应该判为valid = False
                self.valid = False
                return 
        
        self.onPath[i] = False
        self.res.append(i)
        # return 
        
        
