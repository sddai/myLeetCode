# 我们可以将 [0,n−m) 内不可被选的数映射到 [n−m,n−1] 内可选的数上。
'''
在 pick 操作时，我们在 [0,n−m) 范围内进行随机，根据随机值 val 是否为黑名单内数字（是否在 s1 中）进行分情况讨论：
1. 随机值 val 不在 s1 中，说明 val 是真实可选的数值，直接返回；
2. 随机值 val 在 s1 中，说明 val 是黑名单内的数值，我们先查询是否已存在 val 的映射记录，若已存在直接返回其映射值；否则需要在 [n−m,n−1] 内找到一个可替代它的数值，我们可以使用一个变量 idx 在 [n−m,n−1] 范围内从前往后扫描，找到第一个未被使用的，同时不在 s2 中（不在黑名单内）的数字，假设找到的值为 x，将 x 进行返回（同时将 val 与 x 的映射关系，用哈希表进行记录）。—宫水三叶
'''
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = defaultdict(int)
        self.n = n
        map_ = self.map
        # for num in blacklist:
        #     map_[num] = num
        self.m = len(blacklist)
        blackset = set(blacklist)
        m = self.m
        right = n - 1
        for num in blacklist:
            if num >= n - m:
                # right -= 1
                continue
            while right in blackset:
                right -= 1
            map_[num] = right
            right -= 1  
        

        # # self.n = n
        # # self.blacklist = blacklist
        # m = len(blacklist)
        # self.nums = [i for i in range(n)]
        # self.valToIndex = dict()
        # self.size = n
        # for i in self.nums:
        #     self.valToIndex[i] = i
        # right = self.size - 1
        # blackset = set(blacklist)
        # # for blacknum in blacklist:
        # i = 0
        # while i < m:
        #     # print("in loop: ", self.nums, right, i, m)
        #     blacknum = blacklist[i]
        #     if self.valToIndex[blacknum] > right:
        #         continue
        #     while self.nums[right] in blackset:
        #         right -= 1
        #     # if self.valToIndex[blacknum] <= right and self.nums[right ] not in blackset:
        #     if self.valToIndex[blacknum] <= right:
        #         idx = self.valToIndex[blacknum]
        #         self.nums[idx], self.nums[right ] = self.nums[right ], self.nums[idx]
        #         self.valToIndex[blacknum] = right 
        #         self.valToIndex[right ] = blacknum
        #         self.valToIndex.pop(blacknum)
        #         self.nums.pop()
        #         right -= 1
        #         i += 1
        #     # elif self.nums[right] in blackset:  # 要替换的位置也是blacklist，此时往前移动right重新替换
        #     #     right -= 1
        #     #     i += 1
        #     #     continue
        #     # elif self.valToIndex[blacknum] > right: # 要替换的已经在right指针的右侧了，不用替换
        #     #     right -= 1
        #     #     i += 1
        #     #     continue
        # self.right = right  # 这里返回的right是减一之后的right
            

    def pick(self) -> int:
        n = self.n
        m = self.m
        map_ = self.map
        # picked = random.randint(0, n - 1)
        # if picked >= n - m:
        #     picked = map_[picked]
        picked = random.randint(0, n - m - 1)   # 注意最后生成的随机数范围，需要使得所有不在黑名单中的数等可能
        if picked in map_:
            picked = map_[picked]
        return picked
        # print(self.nums, self.right)
        # return self.nums[random.randint(0, self.right )]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()