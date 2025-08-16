# 此题一遍通过
class NumArray:

    def __init__(self, nums: List[int]):
        self.ori_nums = nums.copy()
        self.nums = nums.copy()
        for i in range(len(self.nums)):
            if i == 0:   # 在整体前边加上0，可以避免讨论开头元素的问题
                continue
            self.nums[i] = self.nums[i - 1] + self.nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left] + self.ori_nums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)