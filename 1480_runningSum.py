# 此题一遍通过
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums
        for i in range(1, n):
            nums[i] = nums[i - 1] + nums[i]
        return nums