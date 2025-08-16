# 这里要理解排列和组合的区别：
# 排列可以反向遍历这个数组，也就是，对于[1, 2, 3]，遍历到2的时候，可以反过去将1排到后边（所以for循环从0开始）
# 但是组合与他的区别在于，1,2和2,1是同一个组合（所以for循环从start开始）
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, start):
            if len(path) == n:
                res.append(path[:])
            # for i in range(start, n):   # 排列和组合的区别之一在于这里是从start开始还是从0开始，组合从start开始，排列从0开始
            for i in range(n):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(nums, i + 1)
                path.pop()
                visited[i] = False
        n = len(nums)
        res = []
        path = []
        visited = [False for _ in range(n)]
        dfs(nums, 0)
        return res
    
'''
# 此题第二遍一次通过
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, start, res, used):
            if start >= n:
                res.append(path[:])
            for i in range(start + 1):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(path, i + 1, res, used)
                    path.pop()
                    used[i] = False
            return res
            n = len(nums)
            res = []
            path = []
            start = 0
            used = [False] * n
            return dfs(path, start, res, used)
'''