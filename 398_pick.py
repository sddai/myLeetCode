class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rand = random.Random(0)
        self.findIndex = defaultdict(list)
        for i, num in enumerate(self.nums):
            self.findIndex[num].append(i)


    def pick(self, target: int) -> int:
        return self.rand.choice(self.findIndex[target])
        # 解法二；
        # n = len(self.findIndex[target])
        # return self.findIndex[target][self.rand.randint(0, n - 1)]
        
        # 超时
        # cnt = 0
        # for i, num in enumerate(self.nums):
        #     if num == target:
        #         cnt += 1
        #         if self.rand.randint(0, cnt - 1) == 0:
        #             res = i
        # return res
        # 超时
        # 采用蓄水池采样的方法过不了这道题，测试用例太强了。
        # 每次pick的时间复杂度O(n)，1 <= n<= 210^4，最多有10^4次pick操作
        # 所以总时间复杂度最坏为 210^8，明显超时，已经没有更优的解法了
        # 只能用哈希的方法才能过
        # i = 0
        # cnt = 0
        # res = 0
        # for num in self.nums:
        #     if self.nums[i] == target:
        #         cnt += 1
        #         if self.rand.randint(0, cnt - 1) == 0:
        #             res = i
        #     i += 1
        # return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)