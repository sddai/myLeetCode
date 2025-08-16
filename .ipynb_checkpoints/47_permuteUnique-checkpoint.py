# 全排列问题，以[0, 1, 2, 3]为例：
# 假设当前遍历到1，则在for循环中有i=[0, 1, 2, 3]
# i=0已经标记为used，i=1也是used
# 所以从i=2开始append到path后边
# 所以第一轮下来之后path是[0, 1, 2, 3]
# 然后最里层dfs退出，i=3标记为not used
# 然后倒数第二层的for循环结束
# 再往上一层的for循环，i递增1，也就是原来是[0, 1, ...]，现在这一层的dfs退出来了，for循环递增一，变成了[0, 2, ...]，就是这样不断遍历的
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        def dfs(nums, depth):
            if depth == n:
                res.append(path[:])
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]): # not used[i-1]意味着如果有两个一样的2，如果前一个2没有使用就不使用后一个2，保证了2, 2'和2', 2不会同时计算在path里边
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(nums, depth + 1)
                path.pop()
                used[i] = False
        used = [False for _ in range(n)]
        path = []
        res = []
        dfs(nums, 0)
        return res


'''class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        def dfs(nums, depth):
            if depth == n:
                res.append(path[:])
            for i in range(n):
                # if used[i] == False and (i == 0 or nums[i] != nums[i-1]):# 这里的判断条件易错
                # 当出现重复元素时，比如输入 nums = [1,2,2',2'']，2' 只有在 2 已经被使用的情况下才会被选择，同理，2'' 只有在 2' 已经被使用的情况下才会被选择，这就保证了相同元素在排列中的相对位置保证固定。
                if used[i] == False and (i == 0 or nums[i] != nums[i-1] or used[i-1]):  # 这么写不好，最好通过一个if跳过当前循环（continue）
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums, depth + 1)
                    path.pop()
                    used[i] = False
        used = [False for _ in range(n)]
        path = []
        res = []
        dfs(nums, 0)
        return res
'''