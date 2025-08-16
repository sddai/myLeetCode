# 不必要用并查集
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
def trans_string(s: str) -> str:
    s = s.lower()
    flag = False
    uf = UF(26)
    i = 0
    m = len(s)
    while i < m:
        c = s[i]
        # i += 1
        if c == "(":
            # while s[i + 1] != ")" and s[i + 2] != ")":  # 下标越界
            while i + 2 < m and s[i + 1] != ")" and s[i + 2] != ")":
                uf.union(ord(s[i + 1]) - ord("a"), ord(s[i + 2]) - ord("a"))
                # print("union: ", s[i + 1], s[i + 2])
                # print([uf.parent[i] for i in range(6)])
                i += 1
            # while s[i] != ")" and s[i + 1] != ")":
                # i += 1
        i += 1
    map_char = [[] for _ in range(26)]
    # for i, c in enumerate(uf.parent):  # 【这里不对】
        # map_char[c].append(i)
    for i in range(26):
        c = uf.find(i)
        map_char[c].append(i)
    for alist in map_char:
        alist.sort()
    # print(uf.parent, f"\n", map_char)
    new_s = ""
    use_origin = False
    for i in range(m):
        if s[i] == "(":
            flag = True
        if s[i] == ")":
            flag = False
        if flag:
            continue
        if not flag and s[i] != ")":
            index = ord(s[i]) - ord("a")
            # print(s[i], index)
            # root = uf.parent[index]
            root = uf.find(index)
            replaced = map_char[root][0]
            # print("root, replaced: ", root, replaced)
            if index != replaced:
                # new_s += chr(map_char[root]+ ord("a"))  # 【应该用这个列表中的第一个元素】
                new_s += chr(map_char[root][0]+ ord("a"))
            else:
                new_s += chr(index + ord("a"))
                use_origin = True
    return 0 if not use_origin else new_s
    # for i, c in enumerate(uf.parent):
    #     map_char[i] = uf.parent[i]
    #     if i < map_char[i]:
    #         # uf.parent[i] = i
    #         map_char[i] = i

# s = str(input())
s = "()abd"
print(trans_string(s))
s = "(abd)demand(fb)()for"   # error: 输出 aemanafor,正确答案是：aemanaaor
print(trans_string(s))
s = "()happy(xyz)new(wxy)year(t)"
print(trans_string(s))

# 【分析】s = "(abd)demand(fb)()for"   # error: 输出 aemanafor
# 这个错误是由于，union->abd的时候三者都变成了a，但是union(f, b)的时候，union函数中的root_x = 5, root_y = 0
# 因此，self.parent[root_y] = root_x这句话将a（也就是patent[0]）的parent变成了5，出错
# 具体流程如下：
# root_x, root_y:  0 1
# [0, 0, 2, 3, 4, 5]
# root_x, root_y:  0 3
# [0, 0, 2, 0, 4, 5]
# root_x, root_y:  5 0
# [5, 0, 2, 0, 4, 5]
# 【但是】，从另一个角度去想，这并不是并查集写错了，（已经实现了并查集），但是在判断两个节点是否属于同一个集合的时候，不应该使用==而应该用uf.isConnected()
# 同样的道理，取一个节点的父节点，不应该使用self.parent[]数组，而应该使用uf.find()函数