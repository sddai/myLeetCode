class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sums = sum(i for i in range(n + 1))  # 这个过程可以使用等差数列求和公式：expect = (0 + n) * (n + 1) / 2
        for i in range(n):
            sums -= nums[i]
        return sums