# 此题一遍通过
# 其实不需要按照-x[1]再次排序了：对于几个相交区间合并后的结果区间 x，x.start 一定是这些相交区间中 start 最小的，x.end 一定是这些相交区间中 end 最大的：
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: [x[0], -x[1]])
        l = intervals[0][0]
        r = intervals[0][1]
        res = []
        for i in range(1, n):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            if intervals[i][0] > r:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
        res.append([l, r])
        return res