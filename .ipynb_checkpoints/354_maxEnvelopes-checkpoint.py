# TODO 二分查找的实现：
# 贪心+二分法：
# 原来的dp：dp[i]表示以nums[i]作为“末尾元素”的子序列“长度”
# 现在把函数的自变量因变量反过来：用g[i]表示“长度”为i+1的子序列的最小“末尾元素”（与dp正好相反）
# 在g数组上（g一开始是空的），用二分法找到第一个大于等于nums[i]的下标j，找到j，则修改g[j]为当前这个数，否则这个数加到末尾
# 举例说明：
# [1, 4]
# [1, 3]
# [1, 2]
# [2, 4]
# [2, 3]
# 这个例子中，不用担心对h降序排列之后漏掉较小的h，因为如果最大的好、不满足，LIS算法会继续向下扫描知道找到一个满足要求的h序列，例如这个例子中最后会找到[1, 2]和[2, 4]这样的序列，不用担心[1, 4]屏蔽了后续较小的h值

# 【解法二】贪心 + 二分查找
# 考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 【关键】找出dp中比h_i严格小的最大的元素：我们可以在f上进行二分查找，找出满足要求的 j_0
        # 在遍历所有的h_i之后，f中最后一个有定义的元素的下标增加1（下标从0开始）即为最长严格递增子序列的长度。
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))  # 注意sort的这种写法
        dp = [envelopes[0][1]]
        for i in range(1, n):
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                index = bisect.bisect_left(dp, envelopes[i][1])
                dp[index] = envelopes[i][1]
        return len(dp)


'''
# 这种方法会超时
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))  # 注意sort的这种写法
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                # if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # return dp[-1]   # 【易错】注意这里返回的是每个位置上的dp取最大，而不是dp[-1]
        return max(dp)
'''