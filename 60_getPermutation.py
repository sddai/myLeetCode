'''
# 观察：
1234
1243
1324
1342
1423
1432
2134 ...
第一位的周期是阶乘3!=6，即，当前循环伦次i除以周期6，要取到大于等于商的最小整数（等于6的时候取6/6=1），这个过程用math.ceil实现
【例二】假设n=5：
4!=24
例如n = 5，假设按k选出来的第一位是3，那么，第二位从1245里边选，循环周期是3!=6种
这个时候，由于已经选出来了第一位3，所以要前两组1和2开头的需要减去，也就是k里边要减去2组4!=24，也就是要减去48
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1 for _ in range(n + 1)]
        select = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i
        print(fac)
        res = []
        for i in range(n-1, -1, -1):
            index = math.ceil(k / fac[i])   # 关于这里的数学运算：ceil取大于等于i的最小整数
            res.append(select.pop(index))
            k = k - (index - 1) * fac[i]
            # s[i] = select[k // fac[n - i - 1]]
            # k = k % fac[n - 1 - i]
            # select.pop(s[i] - 1)
        return "".join(str(c) for c in res)
            

    # 超出时间限制        
    # def getPermutation(self, n: int, k: int) -> str:
    #     def dfs(depth):
    #         nonlocal count
    #         nonlocal res
    #         if depth == n:
    #             count += 1
    #             if count == k:
    #                 res = path[:]
    #             return 
    #         for i in range(n):
    #             if used[i] == True:
    #                 continue
    #             path.append(i+1)
    #             used[i] = True
    #             dfs(depth + 1)
    #             path.pop()
    #             used[i] = False
    #     path = []
    #     res = []
    #     count = 0
    #     used = [False for _ in range(n)]# 【注意】记录已经使用过的元素
    #     depth = 0
    #     dfs(depth)
    #     # return res
    #     # return "".join(res)
    #     return "".join(str(s) for s in res)


'''
# 超出时间限制
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(depth):
            if depth == n:
                res.append(path[:])
                return 
            for i in range(n):
                if used[i] == True:
                    continue
                path.append(i+1)
                used[i] = True
                dfs(depth + 1)
                path.pop()
                used[i] = False
        path = []
        res = []
        used = [False for _ in range(n)]# 【注意】记录已经使用过的元素
        depth = 0
        dfs(depth)
        # return res
        return "".join([str(s) for s in res[k-1]])
'''