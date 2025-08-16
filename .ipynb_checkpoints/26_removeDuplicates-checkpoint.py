# 此题一遍通过
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        fast = 0
        pre = float("inf")
        k = 0
        while fast < n:
            if nums[fast] != pre:
                nums[slow] = nums[fast]
                slow += 1
            pre = nums[fast]
            fast += 1
        return slow   # 注意slow不要加1