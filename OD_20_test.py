class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.union_count = n

    def find(self, x):
        # root = x
        # while self.parent[root] != root:
        #     root = self.parent[root]
        
        # root = self.parent[x]
        # while root != x:
        
        if  self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        print("root_x, root_y: ", root_x, root_y)
        if root_x == root_y:
            return 
        # if root_x != root_y:
        
        # root_y = root_x  # 【修改parent应该在class是的数组里边，不能用函数里边的指针】
        # self.parent[y] = root_x  # 【应该是把根节点连起来】
        self.parent[root_y] = root_x
        # self.size[x] += self.size[y]
        # self.size[y] = 0
        self.union_count -= 1
    
    def isConnected(self, x, y):
        # return self.parent[x] == self.parent[y]
        return self.find(x) == self.find(y)




uf = UF(26)
a = "a"
b = "b"
d = "d"
f = "f"
uf.union(ord(a) - ord("a"), ord(b) - ord("a"))
print([uf.parent[i] for i in range(6)])
uf.union(ord(b) - ord("a"), ord(d) - ord("a"))
print([uf.parent[i] for i in range(6)])
uf.union(ord(f) - ord("a"), ord(d) - ord("a"))
print([uf.parent[i] for i in range(6)])