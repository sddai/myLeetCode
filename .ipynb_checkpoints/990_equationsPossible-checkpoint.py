# 注意在函数里边使用find寻找根节点，不要使用parents数组
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
    
        class Union:
            def __init__(self, n):
                self.n = n
                self.parents = [i for i in range(n)]
                self.count = n #   另一种解法是每一组（union）有一个size
                # self.count = [1] * n
            def find(self, x):
                if self.parents[x] != x:
                    # self.parents[x] = self.find(x)   # 这里写错了，直接find(x)会陷入死循环，应该向上找parents[x]
                    # self.parents[x] = self.parents[self.parents[x]]   # 用这种方式，时间复杂度过高O(N),用while
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
            def isConnected(self, x, y):
                # return self.parents[x] == self.parents[y]   # 不要用parents，要用find来判断
                return self.find(x) == self.find(y)
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x == root_y:
                    return
                # else:
                    # self.parents[y] = self.parents[x]
                    # self.count[x] += 1
                self.parents[root_y] = root_x
                self.count -= 1
        
        all_vars = dict()
        i = 0
        for a, _, _, b in equations:
            if a not in all_vars: 
                all_vars[a] = i
                i += 1
            if b not in all_vars:
                all_vars[b] = i
                i += 1
        n = i
        u = Union(n)
        for a, equ, _, b in equations:
            if equ == "=":
                u.union(all_vars[a], all_vars[b])
        for a, equ, _, b in equations:
            if equ == "!":
                if u.isConnected(all_vars[a], all_vars[b]):
                    return False
        return True

            