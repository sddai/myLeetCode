# 背包问题汇总：416 494 1049 474
# 【优化存储】
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        n = len(nums)
        dp = [False for _ in range(target + 1)]
        # dp[i][j]表示前i个数字能否组成和为j的子集
        dp[0] = True
        # for i in range(n + 1):
        #     dp[i][0] = True
        for i in range(1, n + 1):
            # pre = True
            for j in range(target, -1, -1):  # 注意顺序，如果正序递增j，那么，dp[j - nums[i - 1]]会积累True，也就是，当前边一个j-nums[i]为True的时候，下一个j也会为True，但是这时候j已经被用掉一次了，所以j要反过来遍历
            # for j in range(target + 1): # 
                # temp = dp[j]
                if nums[i - 1] > j:
                    dp[j] = dp[j]   # 不装
                else:
                    dp[j] = dp[j - nums[i - 1]] or dp[j]  # 装 or 不装 ，有一种情况为True，结果就为True
                # pre = temp
        return dp[-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        # dp[i][j]表示前i个数字能否组成和为j的子集
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]   # 不装
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]  # 装 or 不装 ，有一种情况为True，结果就为True
        return dp[-1][-1]


'''【直接回溯会超时】
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, start, path, used):
            # print(path)
            # length = len(path)
            # path_sum = sum(path)
            if start == n + 1:
                return False
            if path == target:
                return True
            # if length >= 1 and length < n:
                # if path_sum == total - path_sum:
                    # return True
            for i in range(start, n):
                if not used[i]:
                    path += nums[i]
                    used[i] = True
                    if dfs(nums, start + 1, path, used): return True   # 【易错】【需要格外注意】加上if 和return 是为了在找到一个可行解之后就返回结果，否则算法会一直计算下去，永远返回便利所有情况之后的最后一轮的结果
                    path -= nums[i]
                    used[i] = False
            return False
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1:
            return False
        target = total / 2
        path = 0
        used = [False for _ in range(n)]
        ans = dfs(nums, 0, path, used)
        return ans
'''

        
'''【直接回溯会超时】
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, start, path, used):
            # print(path)
            length = len(path)
            path_sum = sum(path)
            if start == n + 1:
                return False
            if length >= 1 and length < n:
                if path_sum == total - path_sum:
                    return True
            for i in range(start, n):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    if dfs(nums, start + 1, path, used): return True   # 【易错】【需要格外注意】加上if 和return 是为了在找到一个可行解之后就返回结果，否则算法会一直计算下去，永远返回便利所有情况之后的最后一轮的结果
                    path.pop()
                    used[i] = False
            return False
        total = sum(nums)
        n = len(nums)
        path = []
        used = [False for _ in range(n)]
        ans = dfs(nums, 0, path, used)
        return ans
'''