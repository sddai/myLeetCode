# 区间问题类型题，几乎一遍通过
# 此题时间复杂度可以降低到NlogN：只遍历一遍，用rmax记录并更新区间右端点最大值
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0], -x[1]])
        n = len(intervals)
        # l = intervals[0][0]
        r = intervals[0][1]
        res = [False] * n
        # for i in range(1, n):
        ans = 0
        for i in range(1, n):
            for j in range(i, n):
                # if intervals[j][0] <= r:
                if intervals[j][1] <= r:
                    # res += 1
                    res[j] = True
            r = intervals[i][1]
        for i in range(n):
            if res[i]:
                ans += 1
        return n - ans
