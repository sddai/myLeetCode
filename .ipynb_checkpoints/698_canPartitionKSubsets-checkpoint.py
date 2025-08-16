# 创建一个长度为 k 的数组 cur（cur表示k个桶，每个通要装满target的数字），表示当前每个子集的和。
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):   
                # 外层dfs遍历每一个nums中的数字，对于这个数字，尝试放到k个桶中的一个里边，这个桶称为j
                # 如果dfs(i)这个数字放在了i-1号桶中，则桶i和桶i+1的和应该是一样的（因为不再放入数字），这时候剪枝
                if j and cur[j] == cur[j - 1]:
                    continue
                cur[j] += nums[i]
                if cur[j] <= s and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        cur = [0] * k
        nums.sort(reverse=True)
        return dfs(0)


'''
# 按照普通回溯方法会超时
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # @cache
        def dfs(nums, path, start, groups, used, target, k, memo):
            if groups == k:
                # if len(res) == k:
                return True
            # state = str(used)
            
            if path == target:
                # res.append(path)
                # dfs(nums, path, start + 1, groups + 1, used, target)
                # 【易错】!!!这里需要用return返回下一层dfs的结果
                # return 
                res = dfs(nums, 0, 0, groups + 1, used, target, k, memo)  # 注意这里要从0开始从头遍历，path要归零，start也要归零
                memo[used] = res
                return res
                # res.pop()
            if used in memo:
                return memo[used]
            for i in range(start, n):
                # if used[i]:
                if (used >> i) & 1 == 1:
                    continue
                # path.append(nums[i])
                if path + nums[i] > target:    # 注意剪枝，不是if path > target:，而是path+nums[i] > target
                    continue
                path += nums[i]
                # used[i] = True
                used |= 1 << i 
                if dfs(nums, path, start + 1, groups, used, target, k, memo):
                    return True
                # path.pop()
                path -= nums[i]
                # used[i] = False
                used ^= 1 << i
            # if path == 0:
            #     return False
            return False
        n = len(nums)
        nums.sort(reverse = True)
        if k > n:
            return False
        # path = 0
        # start = 0
        # groups = 0
        sumOfNums = sum(nums)
        if sumOfNums % k != 0:
            return False
        target = sumOfNums // k
        if nums[0] > target:
            return False
        used = 0
        memo = dict()
        ans = dfs(nums, 0, 0, 0, used, target, k, memo)
        return ans
'''