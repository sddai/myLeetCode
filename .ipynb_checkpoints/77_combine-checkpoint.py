class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, k):
            nonlocal res 
            nonlocal path
            if len(path) == k:
                res.append(path[:])
                return 
            for i in range(i, n+1):   # 这里每一轮递归的是一个新的起点（i+1）开始到最后的元素
                path.append(i)
                # dfs(n + 1, k)
                dfs(i + 1, k)
                path.pop()
        dfs(1, k)
        return res
