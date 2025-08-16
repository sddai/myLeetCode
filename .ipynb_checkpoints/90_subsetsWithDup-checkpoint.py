# 此题一遍通过
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, start):
            res.append(path[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    # 分析[1, 2, 2']
                    # 第一轮可以遍历到[1, 2, 2']
                    # （因为2'这里是从后边的dfs遍历过来的，2'这里i==start，所以不跳过）
                    # 但是回溯过来以后，由于i递增，2被pop出去，轮到2'的时候，满足跳出条件i>start and nums[i] == nums[i-1]，因此会被跳过，所以[1,2]和[1,2']不会同时出现
                    continue
                path.append(nums[i])
                # print("i=", i, "path=", path)
                dfs(nums, i + 1)
                # print("i=", i, "path=", path)
                path.pop()

        nums.sort()
        n = len(nums)
        path = []
        res = []
        dfs(nums, 0)
        return res