# 【贪心法】求重叠区间类型题
# 此题一遍通过
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        n = len(points)
        count = 1
        bound = points[0][1]
        for i in range(1, n):
            if points[i][0] <= bound:
                continue
            else:
                bound = points[i][1]
                count += 1
        return count