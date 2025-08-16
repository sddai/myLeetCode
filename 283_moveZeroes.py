# 简单题，此题一遍通过
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0
        fast = 0
        while fast < n:
            if 0 == nums[fast]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        while slow < n:
            nums[slow] = 0
            slow += 1