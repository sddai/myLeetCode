# 【贪心法】求重叠区间类型题
# 此题一遍通过
# 考虑所有气球中右边界位置最靠左的那一个，那么一定有一支箭的射出位置就是它的右边界（否则就没有箭可以将其引爆了）
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
    
'''
一定存在一种最优（射出的箭数最小）的方法，使得每一支箭的射出位置都恰好对应着某一个气球的右边界。

这是为什么？我们考虑任意一种最优的方法，对于其中的任意一支箭，我们都通过上面描述的方法，将这支箭的位置移动到它对应的「原本引爆的气球中最靠左的右边界位置」，那么这些原本引爆的气球仍然被引爆。这样一来，所有的气球仍然都会被引爆，并且每一支箭的射出位置都恰好位于某一个气球的右边界了。

作者：力扣官方题解
链接：https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''