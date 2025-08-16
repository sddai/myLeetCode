class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rand = random.Random(0)


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        nums2 = self.nums.copy()
        n = len(nums2)
        for i in range(n):
            i2 = i + self.rand.randint(0, n - i - 1)
            nums2[i], nums2[i2] = nums2[i2], nums2[i]
        return nums2


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()