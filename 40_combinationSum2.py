# 【关键条件】注意：解集不能包含重复的组合。  -> 解决方案：排序，检测c[i]和c[i-1]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, diff, start):
            if diff == 0:
                res.append(path[:])
                return 
            if diff < 0:
                return 
            for i in range(start, n):
                # if i > 0 and candidates[i] == candidates[i-1]:
                if i > start and candidates[i] == candidates[i-1]: 
                    # 注意区分if i > start 和 i > 0 的区别：
                    # i从start开始进行遍历，[1,7]和[1',7]是不需要重复计算的
                    # 但是[1, 1', 6]需要计算在内
                    # [1, 1', 6]能算在内是因为遍历到第一个1的时候不剪枝，所以能遍历到1和1'（因为下一轮不满足i>start，也就是说第二个1不会被剪枝）,但是遍历到1'的时候就会被剪枝，所以[1',1]不会被记录，只记录了[1, 1']
                    continue
                path.append(candidates[i])
                dfs(candidates, diff - candidates[i], i + 1)
                path.pop()
        diff = target
        candidates.sort()
        n = len(candidates)
        res = []
        path = []
        dfs(candidates, diff, 0)
        return res