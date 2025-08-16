# 此题注意n较大，注意超时问题
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        clips = []
        for i in range(n+1):
            clips.append([max(i-ranges[i], 0), min(i+ranges[i], n)])
        clips.sort(key = lambda x: x[0])
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 0
        # for i in range(n+1):    # 这样循环会超时
        #     for start_i, end_i in clips:   # 这样循环会超时
        for start_i, end_i in clips:
            # for start_i, end_i in clips:   # 这样循环会超时
            for i in range(start_i, end_i + 1):
                if i >= start_i and i <= end_i:
                    dp[i] = min(
                        dp[i], 
                        dp[start_i] + 1
                    )
        return dp[-1] if dp[-1] < float("inf") else -1

'''
# 另一种解法【贪心算法】
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        right_most = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(i - ranges[i], 0)
            right_most[left] = max(right_most[left], i + ranges[i])

        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(n):  # 注意这里没有遍历到 n，因为它已经是终点了
            next_right = max(next_right, right_most[i])
            if i == cur_right:  # 到达已建造的桥的右端点
                if i == next_right:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_right = next_right  # 造一座桥
                ans += 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/1/yi-zhang-tu-miao-dong-pythonjavacgo-by-e-wqry/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''