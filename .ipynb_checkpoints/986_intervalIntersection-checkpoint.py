# 涉及到两个序列，用双指针
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        res = []
        i, j = 0, 0
        while i < m and j < n:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right:
                res.append([left, right])
            if secondList[j][1] <= firstList[i][1]:
                j += 1
            else:
                i += 1
        return res