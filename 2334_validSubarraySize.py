# 解题思路：原条件等价于： 子数组最小值 > threshold/k 
# 枚举每个元素作为子数组最小值，单调栈求出作为最小值时左右的影响范围，检查条件是否成立
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        stack = []
        # next_max = [n-1 for _ in range(n)]  # 注意初始值是n
        next_max = [n for _ in range(n)]
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:   # 大于号还是小于号要注意分清楚
                next_max[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []
        # prev_max = [0 for _ in range(n)]
        prev_max = [-1 for _ in range(n)]
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                prev_max[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for i in range(n):
            # k = next_max[i] - prev_max[i] + 1 # 这里错了：k = [left[i]+1,right[i]-1],这是由于单调栈选出来的是下一个比当前值小的索引，为保证nums[i]是最小值，应该使用[left[i]+1,right[i]-1]这两个索引
            k = next_max[i] - prev_max[i] - 1
            if nums[i] > threshold / k:
                return k
        return -1
# 另一种解题思路是并查集，先从大到小给nums排序，然后不断用并查集扩充，直到并查集满足threshold条件（出发点是，k越长，允许的最小值越小）