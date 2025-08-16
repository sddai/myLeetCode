# 【贪心法】求重叠区间类型问题
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        count = 1
        bound = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < bound:
                continue
            else:
                count += 1
                bound = intervals[i][1]
        return n - count
            

        # res = 0
        # n = len(intervals)
        # dp = [[0] * 2 for _ in range(n)]   # dp[i][0]下界   dp[i][1]上界
        # dp[0][0] = intervals[0][0]
        # dp[0][1] = intervals[0][1]
        # for i in range(1, n):
        #     if intervals[i][0] >= dp[i - 1][1]:
        #         dp[i][0] = dp[i - 1][0]
        #         dp[i][1] = intervals[i][1]
        #     if intervals[i][1]