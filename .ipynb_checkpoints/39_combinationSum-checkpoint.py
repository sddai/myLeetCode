# 注意每一轮for循环都从当前节点开始，也就是从i开始，如果从i+1开始，就是节点不可复用，从i开始，说明当前节点在下一轮还可以取到
'''
错误解法（每一轮for循环从0开始）的输出：有重复组合
candidates =
[2,3,6,7]
target =
7
输出
[[2,2,3],[2,3,2],[3,2,2],[7]]
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, diff, start):
            if diff == 0:
                res.append(path[:])
                return 
            if diff < 0:
                return 
            for i in range(start, n):
                path.append(candidates[i])
                dfs(candidates, diff - candidates[i], i)
                path.pop()
        n = len(candidates)
        res = []
        path = []
        diff = target
        dfs(candidates, diff, 0)
        return res