class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.preSum = [0] * (self.n + 1)
        self.randGen = random.Random(0)
        for i in range(self.n):
            self.preSum[i + 1] = w[i] + self.preSum[i]


    def pickIndex(self) -> int:
        # r = self.randGen.randint(0, self.preSum[-1])  # 【注意从1开始】
        # 【思考】为什么从1开始？
        # 例如w = [2, 3]，则总体的权重之和为2+3=5，第一个数字的权重为2/5，第二个数为3/5
        # preSum = [0, 2, 5]
        # 生成的数字的概率空间应该有5种情况，即1、2、3、4、5
        # 在这里边（这个概率空间）选出来小于等于2的情况：包括randint()==1和randint()==2两种，所以满足条件：概率为2/5
        # 归根结底，是因为，preSum的最大值为maxi，则概率空间应该是1~maxi，而不是0~maxi，所以生成的随机数应该先从1开始取值。
        r = self.randGen.randint(1, self.preSum[-1])
        return bisect.bisect_left(self.preSum, r) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()